from interface.tela import Tela
from servicos import ServicosTrekking

from excecoes import (
    CorridaNaoEncontradaError,
    EquipeJaExisteError,
    EquipeNaoEncontradaError,
)


class TelaEquipes(Tela):
    """Tela responsável pelas operações das equipes."""

    def __init__(self, servicos: ServicosTrekking) -> None:
        super().__init__(servicos)

    def exibir(self) -> None:
        """Exibe a listagem de equipes."""
        self.listar()

    def cadastrar(self) -> None:
        """Solicita os dados e cadastra uma equipe."""
        self.mostrar_titulo("CADASTRAR EQUIPE")
        nome = input("Nome da equipe: ")
        try:
            equipe = self._servicos.equipes.cadastrar(nome)
            print(f"Equipe cadastrada: {equipe.nome}")
        except (EquipeJaExisteError, ValueError) as erro:
            print(erro)

    def listar(self) -> None:
        """Exibe todas as equipes cadastradas."""
        self.mostrar_titulo("EQUIPES CADASTRADAS")
        for indice, equipe in enumerate(self._servicos.equipes.listar()):
            print(f"{indice} - {equipe.nome}")

    def consultar(self) -> None:
        """Exibe os dados de uma equipe escolhida pelo usuário."""
        self.mostrar_titulo("CONSULTAR EQUIPE")
        try:
            equipes = self._servicos.equipes.listar()
            for indice, equipe in enumerate(equipes):
                print(f"{indice} - {equipe.nome}")

            equipe = self._servicos.equipes.buscar(
                int(input("Escolha a equipe: "))
            )
            print()
            print(f"Equipe: {equipe.nome}")
            print(f"Corridas: {len(equipe.corridas)}")
            print(f"Passagens: {len(equipe.passagens)}")
        except (ValueError, EquipeNaoEncontradaError) as erro:
            print(erro)

    def adicionar_corrida(self) -> None:
        """Relaciona uma equipe a uma corrida."""
        self.mostrar_titulo("ADICIONAR EQUIPE À CORRIDA")
        try:
            equipes = self._servicos.equipes.listar()
            for indice, equipe in enumerate(equipes):
                print(f"{indice} - {equipe.nome}")
            equipe = self._servicos.equipes.buscar(
                int(input("Escolha a equipe: "))
            )

            print()
            corridas = self._servicos.corridas.listar()
            for indice, corrida in enumerate(corridas):
                print(f"{indice} - {corrida.nome}")
            corrida = self._servicos.corridas.buscar(
                int(input("Escolha a corrida: "))
            )

            self._servicos.equipes.adicionar_a_corrida(equipe, corrida)
            print("Equipe adicionada à corrida.")
        except (
            ValueError,
            EquipeNaoEncontradaError,
            CorridaNaoEncontradaError,
        ) as erro:
            print(erro)

    def historico(self) -> None:
        """Exibe o histórico de passagens de uma equipe."""
        self.mostrar_titulo("HISTÓRICO DA EQUIPE")
        try:
            equipes = self._servicos.equipes.listar()
            for indice, equipe in enumerate(equipes):
                print(f"{indice} - {equipe.nome}")

            equipe = self._servicos.equipes.buscar(
                int(input("Escolha a equipe: "))
            )
            passagens = self._servicos.passagens.listar_por_equipe(equipe)

            if not passagens:
                print("Nenhuma passagem registrada.")
                return

            print(f"Equipe: {equipe.nome}")
            print()
            for passagem in passagens:
                print(
                    f"Checkpoint {passagem.checkpoint.numero} - "
                    f"{passagem.momento}"
                )
        except (ValueError, EquipeNaoEncontradaError) as erro:
            print(erro)
