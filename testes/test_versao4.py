import json
import unittest
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch

from aplicacao import Trekking
from interface.telas.tela_corridas import TelaCorridas
from modelos import Corrida
from servicos import ServicosTrekking


class TesteVersao4(unittest.TestCase):
    def setUp(self):
        self.tmp = TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.diretorio = Path(self.tmp.name)
        self.app = Trekking(self.diretorio)
        self.servicos = ServicosTrekking(self.app)

    def test_validacao_em_modelo_e_servico(self):
        for valor in (0, -5, 1.5, '2', True, None):
            with self.subTest(valor=valor):
                with self.assertRaises(ValueError):
                    Corrida('Inválida', valor)
                with self.assertRaises(ValueError):
                    self.servicos.corridas.cadastrar('Inválida', valor)
        self.assertEqual(len(self.app.corridas), 0)

    def test_consulta_isolada_e_quantidades(self):
        a = self.servicos.corridas.cadastrar('Trilha A', 8)
        b = self.servicos.corridas.cadastrar('Trilha B', 3)
        joao = self.servicos.professores.cadastrar('João')
        maria = self.servicos.professores.cadastrar('Maria')
        self.servicos.checkpoints.cadastrar(2, a, joao)
        self.servicos.checkpoints.cadastrar(1, a, maria)
        self.servicos.checkpoints.cadastrar(1, b, joao)
        self.assertEqual(a.total_checkpoints_previstos, 8)
        self.assertEqual(a.total_checkpoints_com_professores, 2)
        self.assertEqual(self.servicos.corridas.professores_responsaveis(a), ((1, 'Maria'), (2, 'João')))
        self.assertEqual(b.total_checkpoints_com_professores, 1)
        self.assertEqual(self.servicos.corridas.professores_responsaveis(b), ((1, 'João'),))
        tela = TelaCorridas(self.servicos)
        saida = StringIO()
        with redirect_stdout(saida):
            tela.listar()
            with patch('builtins.input', return_value='0'):
                tela.consultar()
        self.assertIn('Previstos: 8', saida.getvalue())
        self.assertIn('Cadastrados com professor responsável: 2', saida.getvalue())
        self.assertIn('Checkpoint 2: João', saida.getvalue())
        self.assertIn('Checkpoint 1: Maria', saida.getvalue())

    def test_sem_responsaveis(self):
        self.servicos.corridas.cadastrar('Vazia', 4)
        tela = TelaCorridas(self.servicos)
        saida = StringIO()
        with redirect_stdout(saida), patch('builtins.input', return_value='0'):
            tela.consultar()
        self.assertIn('Nenhum checkpoint com professor responsável', saida.getvalue())

    def test_persistencia_e_legado(self):
        self.servicos.corridas.cadastrar('Persistente', 9)
        self.assertEqual(json.loads((self.diretorio / 'corridas.json').read_text())[0]['total_checkpoints_previstos'], 9)
        self.assertEqual(Trekking(self.diretorio).corridas[0].total_checkpoints_previstos, 9)
        (self.diretorio / 'corridas.json').write_text('[{"id":1,"nome":"Antiga"}]', encoding='utf-8')
        self.assertEqual(Trekking(self.diretorio).corridas[0].total_checkpoints_previstos, 1)

    def test_interface_nao_cadastra_numero_invalido(self):
        tela = TelaCorridas(self.servicos)
        saida = StringIO()
        with redirect_stdout(saida), patch('builtins.input', side_effect=['Teste', '0']):
            tela.cadastrar()
        self.assertIn('inteiro positivo', saida.getvalue())
        self.assertFalse(self.app.corridas)


if __name__ == '__main__':
    unittest.main()
