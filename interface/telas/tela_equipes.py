from interface.tela import Tela

from excecoes import (
    EquipeJaExisteError,
    EquipeNaoEncontradaError,
    CorridaNaoEncontradaError
)


class TelaEquipes(Tela):
    """
    Tela responsável pelas operações das equipes.
    """

    def exibir(self) -> None:
        self.listar()

    def cadastrar(self) -> None:

        self.mostrar_titulo("CADASTRAR EQUIPE")

        nome = input("Nome da equipe: ")

        try:
            equipe = self._trekking.cadastrar_equipe(nome)

            print(f"Equipe cadastrada: {equipe.nome}")

        except EquipeJaExisteError as erro:
            print(erro)

        except ValueError as erro:
            print(erro)

    def listar(self) -> None:

        self.mostrar_titulo("EQUIPES CADASTRADAS")

        try:
            equipes = self._trekking.listar_equipes()

            for indice, equipe in enumerate(equipes):
                print(f"{indice} - {equipe.nome}")

        except Exception as erro:
            print(erro)

    def consultar(self) -> None:

        self.mostrar_titulo("CONSULTAR EQUIPE")

        try:
            equipes = self._trekking.listar_equipes()

            for indice, equipe in enumerate(equipes):
                print(f"{indice} - {equipe.nome}")

            indice = int(input("Escolha a equipe: "))

            equipe = self._trekking.buscar_equipe(indice)

            print()
            print(f"Equipe: {equipe.nome}")
            print(f"Corridas: {len(equipe.corridas)}")
            print(f"Passagens: {len(equipe.passagens)}")

        except (ValueError, EquipeNaoEncontradaError) as erro:
            print(erro)

    def adicionar_corrida(self) -> None:

        self.mostrar_titulo("ADICIONAR EQUIPE À CORRIDA")

        try:
            equipes = self._trekking.listar_equipes()

            for indice, equipe in enumerate(equipes):
                print(f"{indice} - {equipe.nome}")

            indice_equipe = int(input("Escolha a equipe: "))

            equipe = self._trekking.buscar_equipe(indice_equipe)

            corridas = self._trekking.listar_corridas()

            print()

            for indice, corrida in enumerate(corridas):
                print(f"{indice} - {corrida.nome}")

            indice_corrida = int(input("Escolha a corrida: "))

            corrida = self._trekking.buscar_corrida(indice_corrida)

            self._trekking.adicionar_equipe_corrida(
                equipe,
                corrida
            )

            print("Equipe adicionada à corrida.")

        except (
            ValueError,
            EquipeNaoEncontradaError,
            CorridaNaoEncontradaError
        ) as erro:
            print(erro)

    def historico(self) -> None:

        self.mostrar_titulo("HISTÓRICO DA EQUIPE")

        try:
            equipes = self._trekking.listar_equipes()

            for indice, equipe in enumerate(equipes):
                print(f"{indice} - {equipe.nome}")

            indice = int(input("Escolha a equipe: "))

            equipe = self._trekking.buscar_equipe(indice)

            passagens = self._trekking.listar_passagens_equipe(
                equipe
            )

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