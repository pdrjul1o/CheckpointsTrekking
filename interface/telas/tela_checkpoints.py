from interface.tela import Tela
from servicos import ServicosTrekking

from excecoes import (
    CheckpointJaExisteError,
    CheckpointNaoEncontradoError,
    CorridaNaoEncontradaError,
    ProfessorNaoEncontradoError,
)


class TelaCheckpoints(Tela):
    """Tela responsável pelas operações dos checkpoints."""

    def __init__(self, servicos: ServicosTrekking) -> None:
        super().__init__(servicos)

    def exibir(self) -> None:
        """Exibe a listagem de checkpoints."""
        self.listar()

    def cadastrar(self) -> None:
        """Solicita dados e cadastra um checkpoint."""
        self.mostrar_titulo("CADASTRAR CHECKPOINT")
        try:
            numero = int(input("Número do checkpoint: "))

            print()
            print("Corridas:")
            for indice, corrida in enumerate(self._servicos.corridas.listar()):
                print(f"{indice} - {corrida.nome}")
            corrida = self._servicos.corridas.buscar(
                int(input("Escolha a corrida: "))
            )

            print()
            print("Professores:")
            for indice, professor in enumerate(
                self._servicos.professores.listar()
            ):
                print(f"{indice} - {professor.nome}")
            professor = self._servicos.professores.buscar(
                int(input("Escolha o professor: "))
            )

            checkpoint = self._servicos.checkpoints.cadastrar(
                numero, corrida, professor
            )
            print(f"Checkpoint {checkpoint.numero} cadastrado.")
        except (
            ValueError,
            CorridaNaoEncontradaError,
            ProfessorNaoEncontradoError,
            CheckpointJaExisteError,
        ) as erro:
            print(erro)

    def listar(self) -> None:
        """Exibe todos os checkpoints cadastrados."""
        self.mostrar_titulo("CHECKPOINTS CADASTRADOS")
        for indice, checkpoint in enumerate(self._servicos.checkpoints.listar()):
            print(
                f"{indice} - {checkpoint.numero} - "
                f"{checkpoint.corrida.nome} - {checkpoint.professor.nome}"
            )

    def consultar(self) -> None:
        """Exibe os dados de um checkpoint."""
        self.mostrar_titulo("CONSULTAR CHECKPOINT")
        try:
            for indice, checkpoint in enumerate(
                self._servicos.checkpoints.listar()
            ):
                print(f"{indice} - Checkpoint {checkpoint.numero}")

            checkpoint = self._servicos.checkpoints.buscar(
                int(input("Escolha o checkpoint: "))
            )
            print()
            print(f"Checkpoint: {checkpoint.numero}")
            print(f"Corrida: {checkpoint.corrida.nome}")
            print(f"Professor: {checkpoint.professor.nome}")
        except (ValueError, CheckpointNaoEncontradoError) as erro:
            print(erro)

    def consultar_professor(self) -> None:
        """Exibe o professor responsável por um checkpoint."""
        self.mostrar_titulo("PROFESSOR RESPONSÁVEL")
        try:
            for indice, checkpoint in enumerate(
                self._servicos.checkpoints.listar()
            ):
                print(f"{indice} - Checkpoint {checkpoint.numero}")

            checkpoint = self._servicos.checkpoints.buscar(
                int(input("Escolha o checkpoint: "))
            )
            print(f"Professor: {checkpoint.professor.nome}")
        except (ValueError, CheckpointNaoEncontradoError) as erro:
            print(erro)

    def listar_equipes(self) -> None:
        """Exibe as equipes que passaram por um checkpoint."""
        self.mostrar_titulo("EQUIPES QUE PASSARAM NO CHECKPOINT")
        try:
            for indice, checkpoint in enumerate(
                self._servicos.checkpoints.listar()
            ):
                print(f"{indice} - Checkpoint {checkpoint.numero}")

            checkpoint = self._servicos.checkpoints.buscar(
                int(input("Escolha o checkpoint: "))
            )
            passagens = self._servicos.passagens.listar_por_checkpoint(
                checkpoint
            )

            if not passagens:
                print("Nenhuma equipe passou por esse checkpoint.")
                return

            for passagem in passagens:
                print(f"{passagem.equipe.nome} - {passagem.momento}")
        except (ValueError, CheckpointNaoEncontradoError) as erro:
            print(erro)
