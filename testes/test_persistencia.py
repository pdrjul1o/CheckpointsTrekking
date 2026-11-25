"""Testes de integração com SQLite e ORM, em bancos isolados."""
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from sqlalchemy.exc import IntegrityError
from sqlalchemy import text
from aplicacao import Trekking
from persistencia import configurar_banco
from servicos import ServicosTrekking
from excecoes import (PassagemJaRegistradaError, EquipeNaoParticipanteError,
    CheckpointCorridaInvalidaError, ProfessorCheckpointInvalidoError,
    EquipeJaExisteError, CheckpointJaExisteError)

class TesteORM(unittest.TestCase):
    def setUp(self):
        pasta = TemporaryDirectory()
        self.addCleanup(pasta.cleanup)
        self.pasta = Path(pasta.name)
        self.app = Trekking(self.pasta)
        self.addCleanup(self.app.close)
        self.s = ServicosTrekking(self.app)

    def fluxo(self):
        c = self.s.corridas.cadastrar('Trilha IFRN', 4)
        e = self.s.equipes.cadastrar('Trilheiros')
        p = self.s.professores.cadastrar('Monitor A')
        cp = self.s.checkpoints.cadastrar(1, c, p)
        self.s.equipes.adicionar_a_corrida(e, c)
        return c, e, p, cp

    def test_reinicio_relacionamentos(self):
        c,e,p,cp = self.fluxo()
        x = self.s.passagens.registrar(c,e,cp,p,'09:42')
        self.assertIn(x, self.s.passagens.listar_por_corrida(c))
        self.app.close()
        with Trekking(self.pasta) as a:
            c,e,p,cp,x = a.corridas[0],a.equipes[0],a.professores[0],a.checkpoints[0],a.passagens[0]
            self.assertIn(e,c.equipes)
            self.assertIn(c,e.corridas)
            self.assertIn(cp,p.checkpoints)
            self.assertIs(cp.corrida,c)
            self.assertIs(x.professor,p)
            self.assertIn(x,cp.passagens)
            self.assertEqual(x.momento,'09:42')

    def test_regras(self):
        c,e,p,cp = self.fluxo()
        self.s.equipes.adicionar_a_corrida(e,c)
        self.assertEqual(len(c.equipes),1)
        with self.assertRaises(EquipeJaExisteError): self.s.equipes.cadastrar('trilheiros')
        with self.assertRaises(CheckpointJaExisteError): self.s.checkpoints.cadastrar(1,c,p)
        fora = self.s.equipes.cadastrar('Fora')
        outro = self.s.professores.cadastrar('Outro')
        outra = self.s.corridas.cadastrar('Outra')
        with self.assertRaises(EquipeNaoParticipanteError): self.s.passagens.registrar(c,fora,cp,p,'10:00')
        with self.assertRaises(ProfessorCheckpointInvalidoError): self.s.passagens.registrar(c,e,cp,outro,'10:00')
        with self.assertRaises(CheckpointCorridaInvalidaError): self.s.passagens.registrar(outra,e,cp,p,'10:00')
        self.s.passagens.registrar(c,e,cp,p,'10:00')
        with self.assertRaises(PassagemJaRegistradaError): self.s.passagens.registrar(c,e,cp,p,'10:01')
        self.assertEqual(len(self.s.passagens.listar()),1)

    def test_atualizacao_remocao(self):
        self.fluxo()
        self.s.equipes.cadastrar('Temporária')
        self.s.equipes.atualizar(1,'Renomeada')
        with Trekking(self.pasta) as a: self.assertEqual(a.equipes[1].nome,'Renomeada')
        with self.assertRaises(ValueError): self.s.equipes.remover(0)
        self.s.equipes.remover(1)
        with Trekking(self.pasta) as a: self.assertEqual(len(a.equipes),1)

    def test_fk_ativa(self):
        engine, fabrica = configurar_banco(self.pasta)
        try:
            with fabrica() as sessao:
                with self.assertRaises(IntegrityError):
                    sessao.execute(text('INSERT INTO checkpoint (numero,id_corrida,id_professor) VALUES (1,999,999)'))
                sessao.rollback()
        finally: engine.dispose()

if __name__ == '__main__': unittest.main()
