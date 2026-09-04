from interface.tela import Tela
from servicos import ServicosTrekking

from excecoes import (
    CheckpointCorridaInvalidaError,
    CheckpointNaoEncontradoError,
    CorridaNaoEncontradaError,
    EquipeNaoEncontradaError,
    EquipeNaoParticipanteError,
    PassagemJaRegistradaError,
    ProfessorCheckpointInvalidoError,
)


class TelaPassagens(Tela):
    """Tela responsável pelas operações das passagens."""

    def __init__(self, servicos: ServicosTrekking) -> None:
        super().__init__(servicos)

    def exibir(self) -> None:
        """Exibe a listagem de passagens."""
        self.listar()

    def registrar(self) -> None:
        """Solicita dados e registra uma passagem."""
        self.mostrar_titulo("REGISTRAR PASSAGEM")
        try:
            print("Corridas:")
            for indice, corrida in enumerate(self._servicos.corridas.listar()):
                print(f"{indice} - {corrida.nome}")
            corrida = self._servicos.corridas.buscar(
                int(input("Escolha a corrida: "))
            )

            print()
            print("Equipes:")
            for indice, equipe in enumerate(self._servicos.equipes.listar()):
                print(f"{indice} - {equipe.nome}")
            equipe = self._servicos.equipes.buscar(
                int(input("Escolha a equipe: "))
            )

            print()
            print("Checkpoints da corrida:")
            checkpoints = corrida.checkpoints
            if not checkpoints:
                print("Essa corrida não possui checkpoints.")
                return
            for indice, checkpoint in enumerate(checkpoints):
                print(f"{indice} - Checkpoint {checkpoint.numero}")

            try:
                checkpoint = checkpoints[
                    int(input("Escolha o checkpoint: "))
                ]
            except IndexError as erro:
                raise CheckpointNaoEncontradoError(
                    "Checkpoint inválido."
                ) from erro

            print(f"Professor responsável: {checkpoint.professor.nome}")
            momento = input("Momento da passagem (ex: 09:42): ")

            passagem = self._servicos.passagens.registrar(
                corrida,
                equipe,
                checkpoint,
                checkpoint.professor,
                momento,
            )

            print()
            print("Passagem registrada:")
            print(passagem)
        except (
            ValueError,
            CorridaNaoEncontradaError,
            EquipeNaoEncontradaError,
            CheckpointCorridaInvalidaError,
    CheckpointNaoEncontradoError,
            EquipeNaoParticipanteError,
            PassagemJaRegistradaError,
    ProfessorCheckpointInvalidoError,
        ) as erro:
            print(erro)

    def listar(self) -> None:
        """Exibe todas as passagens registradas."""
        self.mostrar_titulo("PASSAGENS REGISTRADAS")
        for indice, passagem in enumerate(self._servicos.passagens.listar()):
            print(f"{indice} - {passagem}")

    def listar_corrida(self) -> None:
        """Exibe as passagens de uma corrida."""
        self.mostrar_titulo("PASSAGENS DA CORRIDA")
        try:
            for indice, corrida in enumerate(self._servicos.corridas.listar()):
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

    def progressao_equipe(self) -> None:
        """Exibe a progressão registrada de uma equipe."""
        self.mostrar_titulo("PROGRESSÃO DA EQUIPE")
        try:
            for indice, equipe in enumerate(self._servicos.equipes.listar()):
                print(f"{indice} - {equipe.nome}")
            equipe = self._servicos.equipes.buscar(
                int(input("Escolha a equipe: "))
            )
            if not equipe.passagens:
                print("Nenhuma passagem registrada.")
                return

            print()
            print(f"Equipe: {equipe.nome}")
            print()
            for passagem in equipe.passagens:
                print(
                    f"Checkpoint {passagem.checkpoint.numero} - "
                    f"{passagem.momento}"
                )
        except (ValueError, EquipeNaoEncontradaError) as erro:
            print(erro)

    def listar_checkpoint(self) -> None:
        """Exibe as passagens de um checkpoint."""
        self.mostrar_titulo("PASSAGENS DO CHECKPOINT")
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
                print("Nenhuma passagem registrada.")
                return
            for passagem in passagens:
                print(
                    f"{passagem.equipe.nome} - {passagem.momento}"
                )
        except (ValueError, CheckpointNaoEncontradoError) as erro:
            print(erro)

    def historico_equipe(self) -> None:
        """Exibe o histórico de uma equipe."""
        self.mostrar_titulo("HISTÓRICO DA EQUIPE")
        try:
            for indice, equipe in enumerate(self._servicos.equipes.listar()):
                print(f"{indice} - {equipe.nome}")
            equipe = self._servicos.equipes.buscar(
                int(input("Escolha a equipe: "))
            )
            passagens = self._servicos.passagens.listar_por_equipe(equipe)

            if not passagens:
                print("Nenhuma passagem registrada.")
                return

            for passagem in passagens:
                print(f"Corrida: {passagem.corrida.nome}")
                print(f"Checkpoint: {passagem.checkpoint.numero}")
                print(f"Horário: {passagem.momento}")
                print()
        except (ValueError, EquipeNaoEncontradaError) as erro:
            print(erro)
