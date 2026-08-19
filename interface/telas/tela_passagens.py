from interface.tela import Tela

from excecoes import (
    CorridaNaoEncontradaError,
    EquipeNaoEncontradaError,
    CheckpointNaoEncontradoError,
    ProfessorNaoEncontradoError,
    EquipeNaoParticipanteError,
    PassagemJaRegistradaError
)


class TelaPassagens(Tela):
    """
    Tela responsável pelas operações das passagens.
    """

    def exibir(self) -> None:
        self.listar()

    def registrar(self) -> None:

        self.mostrar_titulo("REGISTRAR PASSAGEM")

        try:
            corridas = self._trekking.listar_corridas()

            print("Corridas:")

            for indice, corrida in enumerate(corridas):
                print(f"{indice} - {corrida.nome}")

            indice_corrida = int(
                input("Escolha a corrida: ")
            )

            corrida = self._trekking.buscar_corrida(
                indice_corrida
            )

            equipes = self._trekking.listar_equipes()

            print()
            print("Equipes:")

            for indice, equipe in enumerate(equipes):
                print(f"{indice} - {equipe.nome}")

            indice_equipe = int(
                input("Escolha a equipe: ")
            )

            equipe = self._trekking.buscar_equipe(
                indice_equipe
            )

            checkpoints = corrida.checkpoints

            print()
            print("Checkpoints da corrida:")

            for indice, checkpoint in enumerate(checkpoints):
                print(
                    f"{indice} - "
                    f"Checkpoint {checkpoint.numero}"
                )

            indice_checkpoint = int(
                input("Escolha o checkpoint: ")
            )

            checkpoint = checkpoints[indice_checkpoint]

            print()
            print(
                f"Professor responsável: "
                f"{checkpoint.professor.nome}"
            )

            momento = input(
                "Momento da passagem (ex: 09:42): "
            )

            passagem = self._trekking.registrar_passagem(
                corrida,
                equipe,
                checkpoint,
                checkpoint.professor,
                momento
            )

            print()
            print("Passagem registrada:")
            print(passagem)

        except (
            ValueError,
            CorridaNaoEncontradaError,
            EquipeNaoEncontradaError,
            CheckpointNaoEncontradoError,
            ProfessorNaoEncontradoError,
            EquipeNaoParticipanteError,
            PassagemJaRegistradaError
        ) as erro:
            print(erro)

    def listar(self) -> None:

        self.mostrar_titulo("PASSAGENS REGISTRADAS")

        try:
            passagens = self._trekking.listar_passagens()

            for indice, passagem in enumerate(passagens):
                print(
                    f"{indice} - {passagem}"
                )

        except Exception as erro:
            print(erro)

    def listar_corrida(self) -> None:

        self.mostrar_titulo(
            "PASSAGENS DA CORRIDA"
        )

        try:
            corridas = self._trekking.listar_corridas()

            for indice, corrida in enumerate(corridas):
                print(f"{indice} - {corrida.nome}")

            indice = int(
                input("Escolha a corrida: ")
            )

            corrida = self._trekking.buscar_corrida(indice)

            passagens = self._trekking.listar_passagens_corrida(
                corrida
            )

            if not passagens:
                print("Nenhuma passagem registrada.")
                return

            for passagem in passagens:
                print(passagem)

        except (
            ValueError,
            CorridaNaoEncontradaError
        ) as erro:
            print(erro)

    def progressao_equipe(self) -> None:

        self.mostrar_titulo(
            "PROGRESSÃO DA EQUIPE"
        )

        try:
            equipes = self._trekking.listar_equipes()

            for indice, equipe in enumerate(equipes):
                print(f"{indice} - {equipe.nome}")

            indice = int(
                input("Escolha a equipe: ")
            )

            equipe = self._trekking.buscar_equipe(indice)

            if not equipe.passagens:
                print(
                    "Nenhuma passagem registrada."
                )
                return

            print()
            print(f"Equipe: {equipe.nome}")
            print()

            for passagem in equipe.passagens:
                print(
                    f"Checkpoint "
                    f"{passagem.checkpoint.numero} - "
                    f"{passagem.momento}"
                )

        except (
            ValueError,
            EquipeNaoEncontradaError
        ) as erro:
            print(erro)

    def listar_checkpoint(self) -> None:

        self.mostrar_titulo(
            "PASSAGENS DO CHECKPOINT"
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

            passagens = (
                self._trekking.listar_passagens_checkpoint(
                    checkpoint
                )
            )

            if not passagens:
                print(
                    "Nenhuma passagem registrada."
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

    def historico_equipe(self) -> None:

        self.mostrar_titulo(
            "HISTÓRICO DA EQUIPE"
        )

        try:
            equipes = self._trekking.listar_equipes()

            for indice, equipe in enumerate(equipes):
                print(f"{indice} - {equipe.nome}")

            indice = int(
                input("Escolha a equipe: ")
            )

            equipe = self._trekking.buscar_equipe(indice)

            passagens = self._trekking.listar_passagens_equipe(
                equipe
            )

            if not passagens:
                print(
                    "Nenhuma passagem registrada."
                )
                return

            for passagem in passagens:
                print(
                    f"Corrida: {passagem.corrida.nome}"
                )
                print(
                    f"Checkpoint: "
                    f"{passagem.checkpoint.numero}"
                )
                print(
                    f"Horário: {passagem.momento}"
                )
                print()

        except (
            ValueError,
            EquipeNaoEncontradaError
        ) as erro:
            print(erro)