from interface.tela import Tela

from excecoes import (
    ProfessorJaExisteError,
    ProfessorNaoEncontradoError
)


class TelaProfessores(Tela):
    """
    Tela responsável pelas operações dos professores.
    """

    def exibir(self) -> None:
        self.listar()

    def cadastrar(self) -> None:

        self.mostrar_titulo("CADASTRAR PROFESSOR")

        nome = input("Nome do professor: ")

        try:
            professor = self._trekking.cadastrar_professor(nome)

            print(
                f"Professor cadastrado: {professor.nome}"
            )

        except ProfessorJaExisteError as erro:
            print(erro)

        except ValueError as erro:
            print(erro)

    def listar(self) -> None:

        self.mostrar_titulo("PROFESSORES CADASTRADOS")

        try:
            professores = self._trekking.listar_professores()

            for indice, professor in enumerate(professores):
                print(f"{indice} - {professor.nome}")

        except Exception as erro:
            print(erro)

    def consultar(self) -> None:

        self.mostrar_titulo("CONSULTAR PROFESSOR")

        try:
            professores = self._trekking.listar_professores()

            for indice, professor in enumerate(professores):
                print(f"{indice} - {professor.nome}")

            indice = int(input("Escolha o professor: "))

            professor = self._trekking.buscar_professor(indice)

            print()
            print(f"Professor: {professor.nome}")
            print(
                f"Checkpoints: {len(professor.checkpoints)}"
            )

        except (
            ValueError,
            ProfessorNaoEncontradoError
        ) as erro:
            print(erro)

    def listar_checkpoints(self) -> None:

        self.mostrar_titulo("CHECKPOINTS DO PROFESSOR")

        try:
            professores = self._trekking.listar_professores()

            for indice, professor in enumerate(professores):
                print(f"{indice} - {professor.nome}")

            indice = int(input("Escolha o professor: "))

            professor = self._trekking.buscar_professor(indice)

            if not professor.checkpoints:
                print(
                    "Esse professor não possui checkpoints."
                )
                return

            for checkpoint in professor.checkpoints:
                print(
                    f"Checkpoint {checkpoint.numero} - "
                    f"Corrida: {checkpoint.corrida.nome}"
                )

        except (
            ValueError,
            ProfessorNaoEncontradoError
        ) as erro:
            print(erro)