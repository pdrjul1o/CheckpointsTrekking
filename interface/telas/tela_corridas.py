from interface.tela import Tela

from excecoes import CorridaJaExisteError, CorridaNaoEncontradaError


class TelaCorridas(Tela):
    """
    Tela responsável pelas operações das corridas.
    """

    def exibir(self) -> None:
        self.listar()

    def cadastrar(self) -> None:

        self.mostrar_titulo("CADASTRAR CORRIDA")

        nome = input("Nome da corrida: ")

        try:
            corrida = self._trekking.cadastrar_corrida(nome)

            print(f"Corrida cadastrada: {corrida.nome}")

        except CorridaJaExisteError as erro:
            print(erro)

        except ValueError as erro:
            print(erro)

    def listar(self) -> None:

        self.mostrar_titulo("CORRIDAS CADASTRADAS")

        try:
            corridas = self._trekking.listar_corridas()

            for indice, corrida in enumerate(corridas):
                print(f"{indice} - {corrida.nome}")

        except Exception as erro:
            print(erro)

    def consultar(self) -> None:

        self.mostrar_titulo("CONSULTAR CORRIDA")

        try:
            corridas = self._trekking.listar_corridas()

            for indice, corrida in enumerate(corridas):
                print(f"{indice} - {corrida.nome}")

            indice = int(input("Escolha a corrida: "))

            corrida = self._trekking.buscar_corrida(indice)

            print()
            print(f"Corrida: {corrida.nome}")
            print(f"Checkpoints: {len(corrida.checkpoints)}")

        except (ValueError, CorridaNaoEncontradaError) as erro:
            print(erro)

    def listar_checkpoints(self) -> None:

        self.mostrar_titulo("CHECKPOINTS DA CORRIDA")

        try:
            corridas = self._trekking.listar_corridas()

            for indice, corrida in enumerate(corridas):
                print(f"{indice} - {corrida.nome}")

            indice = int(input("Escolha a corrida: "))

            corrida = self._trekking.buscar_corrida(indice)

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

        self.mostrar_titulo("PASSAGENS DA CORRIDA")

        try:
            corridas = self._trekking.listar_corridas()

            for indice, corrida in enumerate(corridas):
                print(f"{indice} - {corrida.nome}")

            indice = int(input("Escolha a corrida: "))

            corrida = self._trekking.buscar_corrida(indice)

            passagens = self._trekking.listar_passagens_corrida(corrida)

            if not passagens:
                print("Nenhuma passagem registrada.")
                return

            for passagem in passagens:
                print(passagem)

        except (ValueError, CorridaNaoEncontradaError) as erro:
            print(erro)