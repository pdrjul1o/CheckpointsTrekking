from interface.tela import Tela
from servicos import ServicosTrekking

from excecoes import CorridaJaExisteError, CorridaNaoEncontradaError


class TelaCorridas(Tela):
    """Tela responsável pelas operações das corridas."""

    def __init__(self, servicos: ServicosTrekking) -> None:
        super().__init__(servicos)

    def exibir(self) -> None:
        """Exibe a listagem de corridas."""
        self.listar()

    def cadastrar(self) -> None:
        """Solicita os dados e cadastra uma corrida."""
        self.mostrar_titulo("CADASTRAR CORRIDA")
        nome = input("Nome da corrida: ")

        try:
            corrida = self._servicos.corridas.cadastrar(nome)
            print(f"Corrida cadastrada: {corrida.nome}")
        except (CorridaJaExisteError, ValueError) as erro:
            print(erro)

    def listar(self) -> None:
        """Exibe todas as corridas cadastradas."""
        self.mostrar_titulo("CORRIDAS CADASTRADAS")
        for indice, corrida in enumerate(self._servicos.corridas.listar()):
            print(f"{indice} - {corrida.nome}")

    def consultar(self) -> None:
        """Exibe os dados de uma corrida escolhida pelo usuário."""
        self.mostrar_titulo("CONSULTAR CORRIDA")
        try:
            corridas = self._servicos.corridas.listar()
            for indice, corrida in enumerate(corridas):
                print(f"{indice} - {corrida.nome}")

            indice = int(input("Escolha a corrida: "))
            corrida = self._servicos.corridas.buscar(indice)

            print()
            print(f"Corrida: {corrida.nome}")
            print(f"Checkpoints: {len(corrida.checkpoints)}")
        except (ValueError, CorridaNaoEncontradaError) as erro:
            print(erro)

    def listar_checkpoints(self) -> None:
        """Exibe os checkpoints de uma corrida."""
        self.mostrar_titulo("CHECKPOINTS DA CORRIDA")
        try:
            corridas = self._servicos.corridas.listar()
            for indice, corrida in enumerate(corridas):
                print(f"{indice} - {corrida.nome}")

            corrida = self._servicos.corridas.buscar(
                int(input("Escolha a corrida: "))
            )

            if not corrida.checkpoints:
                print("Essa corrida não possui checkpoints.")
                return

            for checkpoint in corrida.checkpoints:
                print(
                    f"Checkpoint {checkpoint.numero} - "
                    f"Professor: {checkpoint.professor.nome}"
                )
        except (ValueError, CorridaNaoEncontradaError) as erro:
            print(erro)

    def listar_passagens(self) -> None:
        """Exibe as passagens registradas em uma corrida."""
        self.mostrar_titulo("PASSAGENS DA CORRIDA")
        try:
            corridas = self._servicos.corridas.listar()
            for indice, corrida in enumerate(corridas):
                print(f"{indice} - {corrida.nome}")

            corrida = self._servicos.corridas.buscar(
                int(input("Escolha a corrida: "))
            )
            passagens = self._servicos.passagens.listar_por_corrida(corrida)

            if not passagens:
                print("Nenhuma passagem registrada.")
                return

            for passagem in passagens:
                print(passagem)
        except (ValueError, CorridaNaoEncontradaError) as erro:
            print(erro)
