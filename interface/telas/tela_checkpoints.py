from interface.tela import Tela

from excecoes import (
    CheckpointNaoEncontradoError,
    CorridaNaoEncontradaError,
    ProfessorNaoEncontradoError
)


class TelaCheckpoints(Tela):
    """
    Tela responsável pelas operações dos checkpoints.
    """

    def exibir(self) -> None:
        self.listar()

    def cadastrar(self) -> None:

        self.mostrar_titulo("CADASTRAR CHECKPOINT")

        try:
            numero = int(
                input("Número do checkpoint: ")
            )

            corridas = self._trekking.listar_corridas()

            print()
            print("Corridas:")

            for indice, corrida in enumerate(corridas):
                print(f"{indice} - {corrida.nome}")

            indice_corrida = int(
                input("Escolha a corrida: ")
            )

            corrida = self._trekking.buscar_corrida(
                indice_corrida
            )

            professores = self._trekking.listar_professores()

            print()
            print("Professores:")

            for indice, professor in enumerate(professores):
                print(f"{indice} - {professor.nome}")

            indice_professor = int(
                input("Escolha o professor: ")
            )

            professor = self._trekking.buscar_professor(
                indice_professor
            )

            checkpoint = self._trekking.cadastrar_checkpoint(
                numero,
                corrida,
                professor
            )

            print(
                f"Checkpoint {checkpoint.numero} cadastrado."
            )

        except (
            ValueError,
            CorridaNaoEncontradaError,
            ProfessorNaoEncontradoError
        ) as erro:
            print(erro)

    def listar(self) -> None:

        self.mostrar_titulo("CHECKPOINTS CADASTRADOS")

        try:
            checkpoints = self._trekking.listar_checkpoints()

            for indice, checkpoint in enumerate(checkpoints):
                print(
                    f"{indice} - "
                    f"{checkpoint.numero} - "
                    f"{checkpoint.corrida.nome} - "
                    f"{checkpoint.professor.nome}"
                )

        except Exception as erro:
            print(erro)

    def consultar(self) -> None:

        self.mostrar_titulo("CONSULTAR CHECKPOINT")

        try:
            checkpoints = self._trekking.listar_checkpoints()

            for indice, checkpoint in enumerate(checkpoints):
                print(
                    f"{indice} - "
                    f"Checkpoint {checkpoint.numero}"
                )

            indice = int(
                input("Escolha o checkpoint: ")
            )

            checkpoint = self._trekking.buscar_checkpoint(
                indice
            )

            print()
            print(f"Checkpoint: {checkpoint.numero}")
            print(f"Corrida: {checkpoint.corrida.nome}")
            print(
                f"Professor: {checkpoint.professor.nome}"
            )

        except (
            ValueError,
            CheckpointNaoEncontradoError
        ) as erro:
            print(erro)

    def consultar_professor(self) -> None:

        self.mostrar_titulo(
            "PROFESSOR RESPONSÁVEL"
        )

        try:
            checkpoints = self._trekking.listar_checkpoints()

            for indice, checkpoint in enumerate(checkpoints):
                print(
                    f"{indice} - "
                    f"Checkpoint {checkpoint.numero}"
                )

            indice = int(
                input("Escolha o checkpoint: ")
            )

            checkpoint = self._trekking.buscar_checkpoint(
                indice
            )

            print(
                f"Professor: {checkpoint.professor.nome}"
            )

        except (
            ValueError,
            CheckpointNaoEncontradoError
        ) as erro:
            print(erro)

    def listar_equipes(self) -> None:

        self.mostrar_titulo(
            "EQUIPES QUE PASSARAM NO CHECKPOINT"
        )

        try:
            checkpoints = self._trekking.listar_checkpoints()

            for indice, checkpoint in enumerate(checkpoints):
                print(
                    f"{indice} - "
                    f"Checkpoint {checkpoint.numero}"
                )

            indice = int(
                input("Escolha o checkpoint: ")
            )

            checkpoint = self._trekking.buscar_checkpoint(
                indice
            )

            passagens = self._trekking.listar_passagens_checkpoint(
                checkpoint
            )

            if not passagens:
                print(
                    "Nenhuma equipe passou por esse checkpoint."
                )
                return

            for passagem in passagens:
                print(
                    f"{passagem.equipe.nome} - "
                    f"{passagem.momento}"
                )

        except (
            ValueError,
            CheckpointNaoEncontradoError
        ) as erro:
            print(erro)