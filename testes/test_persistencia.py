"""Testes da terceira versão: gravação, recarga e falhas de persistência."""
import json
from pathlib import Path
from tempfile import TemporaryDirectory

from aplicacao import Trekking
from excecoes import PassagemJaRegistradaError
from persistencia import ErroPersistencia
from servicos import ServicosTrekking


def testar_reinicio_e_relacionamentos() -> None:
    """Cadastra, grava, reinicia e recupera relações entre os objetos."""
    with TemporaryDirectory() as pasta:
        diretorio = Path(pasta)
        app = Trekking(diretorio)
        servicos = ServicosTrekking(app)
        corrida = servicos.corridas.cadastrar('Trilha Persistente')
        equipe = servicos.equipes.cadastrar('Equipe Aurora')
        professor = servicos.professores.cadastrar('Professor Paulo')
        checkpoint = servicos.checkpoints.cadastrar(1, corrida, professor)
        servicos.equipes.adicionar_a_corrida(equipe, corrida)
        servicos.passagens.registrar(corrida, equipe, checkpoint, professor, '10:15')

        recarregada = Trekking(diretorio)
        nova_corrida, = recarregada.corridas
        nova_equipe, = recarregada.equipes
        novo_professor, = recarregada.professores
        novo_checkpoint, = recarregada.checkpoints
        nova_passagem, = recarregada.passagens
        assert nova_corrida in nova_equipe.corridas
        assert nova_equipe in nova_corrida.equipes
        assert novo_checkpoint.corrida is nova_corrida
        assert novo_checkpoint.professor is novo_professor
        assert nova_passagem in nova_corrida.passagens
        assert nova_passagem in nova_equipe.passagens
        assert nova_passagem in novo_checkpoint.passagens
        assert nova_passagem.professor is novo_professor
        try:
            ServicosTrekking(recarregada).passagens.registrar(nova_corrida, nova_equipe, novo_checkpoint, novo_professor, '11:00')
        except PassagemJaRegistradaError:
            pass
        else:
            raise AssertionError('Registro duplicado deveria ser rejeitado')


def testar_arquivo_invalido() -> None:
    """Rejeita JSON corrompido sem descartar os dados anteriores."""
    with TemporaryDirectory() as pasta:
        diretorio = Path(pasta)
        Trekking(diretorio)
        (diretorio / 'equipes.json').write_text('{invalid', encoding='utf-8')
        try:
            Trekking(diretorio)
        except ErroPersistencia:
            pass
        else:
            raise AssertionError('JSON inválido deveria ser rejeitado')


def testar_referencia_inexistente() -> None:
    """Rejeita registros que referenciam entidades ausentes."""
    with TemporaryDirectory() as pasta:
        diretorio = Path(pasta)
        Trekking(diretorio)
        (diretorio / 'equipes.json').write_text(json.dumps([{'id': 1, 'nome': 'Sem corrida', 'corrida_ids': [99]}]), encoding='utf-8')
        try:
            Trekking(diretorio)
        except ErroPersistencia:
            pass
        else:
            raise AssertionError('Referência inexistente deveria ser rejeitada')


if __name__ == '__main__':
    testar_reinicio_e_relacionamentos()
    testar_arquivo_invalido()
    testar_referencia_inexistente()
    print('Testes de persistência da terceira versão passaram.')
