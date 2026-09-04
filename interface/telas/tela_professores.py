from interface.tela import Tela
from servicos import ServicosTrekking

from excecoes import ProfessorJaExisteError, ProfessorNaoEncontradoError


class TelaProfessores(Tela):
    """Tela responsável pelas operações dos professores."""

    def __init__(self, servicos: ServicosTrekking) -> None:
        super().__init__(servicos)

    def exibir(self) -> None:
        """Exibe a listagem de professores."""
        self.listar()

    def cadastrar(self) -> None:
        """Solicita os dados e cadastra um professor."""
        self.mostrar_titulo("CADASTRAR PROFESSOR")
        nome = input("Nome do professor: ")
        try:
            professor = self._servicos.professores.cadastrar(nome)
            print(f"Professor cadastrado: {professor.nome}")
        except (ProfessorJaExisteError, ValueError) as erro:
            print(erro)

    def listar(self) -> None:
        """Exibe todos os professores cadastrados."""
        self.mostrar_titulo("PROFESSORES CADASTRADOS")
        for indice, professor in enumerate(self._servicos.professores.listar()):
            print(f"{indice} - {professor.nome}")

    def consultar(self) -> None:
        """Exibe os dados de um professor escolhido."""
        self.mostrar_titulo("CONSULTAR PROFESSOR")
        try:
            professores = self._servicos.professores.listar()
            for indice, professor in enumerate(professores):
                print(f"{indice} - {professor.nome}")

            professor = self._servicos.professores.buscar(
                int(input("Escolha o professor: "))
            )
            print()
            print(f"Professor: {professor.nome}")
            print(f"Checkpoints: {len(professor.checkpoints)}")
        except (ValueError, ProfessorNaoEncontradoError) as erro:
            print(erro)

    def listar_checkpoints(self) -> None:
        """Exibe os checkpoints sob responsabilidade do professor."""
        self.mostrar_titulo("CHECKPOINTS DO PROFESSOR")
        try:
            professores = self._servicos.professores.listar()
            for indice, professor in enumerate(professores):
                print(f"{indice} - {professor.nome}")

            professor = self._servicos.professores.buscar(
                int(input("Escolha o professor: "))
            )

            if not professor.checkpoints:
                print("Esse professor não possui checkpoints.")
                return

            for checkpoint in professor.checkpoints:
                print(
                    f"Checkpoint {checkpoint.numero} - "
                    f"Corrida: {checkpoint.corrida.nome}"
                )
        except (ValueError, ProfessorNaoEncontradoError) as erro:
            print(erro)
