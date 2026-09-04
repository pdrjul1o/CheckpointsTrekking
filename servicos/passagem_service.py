from aplicacao import Trekking
from excecoes import (
    CheckpointCorridaInvalidaError,
    CheckpointNaoEncontradoError,
    CorridaNaoEncontradaError,
    EquipeNaoEncontradaError,
    EquipeNaoParticipanteError,
    PassagemJaRegistradaError,
    ProfessorCheckpointInvalidoError,
    ProfessorNaoEncontradoError,
)
from modelos import Checkpoint, Corrida, Equipe, Passagem, Professor


class PassagemService:
    """Coordena o registro e as consultas de passagens."""

    def __init__(self, aplicacao: Trekking) -> None:
        """Inicializa o serviço com a aplicação que mantém os dados."""
        self.__aplicacao = aplicacao

    def registrar(
        self,
        corrida: Corrida,
        equipe: Equipe,
        checkpoint: Checkpoint,
        professor: Professor,
        momento: str,
    ) -> Passagem:
        """Valida as regras e registra uma passagem de equipe."""
        if corrida not in self.__aplicacao.corridas:
            raise CorridaNaoEncontradaError("Corrida não encontrada.")
        if equipe not in self.__aplicacao.equipes:
            raise EquipeNaoEncontradaError("Equipe não encontrada.")
        if checkpoint not in self.__aplicacao.checkpoints:
            raise CheckpointNaoEncontradoError("Checkpoint não encontrado.")
        if professor not in self.__aplicacao.professores:
            raise ProfessorNaoEncontradoError("Professor não encontrado.")

        if checkpoint.corrida != corrida:
            raise CheckpointCorridaInvalidaError(
                "O checkpoint não pertence a essa corrida."
            )
        if checkpoint.professor != professor:
            raise ProfessorCheckpointInvalidoError(
                "O professor não é responsável por esse checkpoint."
            )
        if corrida not in equipe.corridas:
            raise EquipeNaoParticipanteError(
                "A equipe não participa dessa corrida."
            )

        for passagem in self.__aplicacao.passagens:
            if (
                passagem.corrida == corrida
                and passagem.equipe == equipe
                and passagem.checkpoint == checkpoint
            ):
                raise PassagemJaRegistradaError(
                    "Essa equipe já passou por esse checkpoint."
                )

        momento = momento.strip()
        if not momento:
            raise ValueError("O momento da passagem não pode ser vazio.")

        passagem = Passagem(
            corrida,
            equipe,
            checkpoint,
            professor,
            momento,
        )
        self.__aplicacao.adicionar_passagem(passagem)

        corrida.adicionar_passagem(passagem)
        equipe.adicionar_passagem(passagem)
        checkpoint.adicionar_passagem(passagem)

        return passagem

    def listar(self) -> tuple[Passagem, ...]:
        """Retorna todas as passagens registradas."""
        return self.__aplicacao.passagens

    def listar_por_corrida(self, corrida: Corrida) -> list[Passagem]:
        """Retorna as passagens pertencentes a uma corrida."""
        return [
            passagem
            for passagem in self.__aplicacao.passagens
            if passagem.corrida == corrida
        ]

    def listar_por_equipe(self, equipe: Equipe) -> list[Passagem]:
        """Retorna as passagens registradas por uma equipe."""
        return [
            passagem
            for passagem in self.__aplicacao.passagens
            if passagem.equipe == equipe
        ]

    def listar_por_checkpoint(
        self,
        checkpoint: Checkpoint,
    ) -> list[Passagem]:
        """Retorna as passagens registradas em um checkpoint."""
        return [
            passagem
            for passagem in self.__aplicacao.passagens
            if passagem.checkpoint == checkpoint
        ]
