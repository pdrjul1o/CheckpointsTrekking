from aplicacao import Trekking
from excecoes import (
    CheckpointJaExisteError,
    CheckpointNaoEncontradoError,
    CorridaNaoEncontradaError,
    ProfessorNaoEncontradoError,
)
from modelos import Checkpoint, Corrida, Professor


class CheckpointService:
    """Coordena o cadastro e as consultas de checkpoints."""

    def __init__(self, aplicacao: Trekking) -> None:
        """Inicializa o serviço com a aplicação que mantém os dados."""
        self.__aplicacao = aplicacao

    def cadastrar(
        self,
        numero: int,
        corrida: Corrida,
        professor: Professor,
    ) -> Checkpoint:
        """Cadastra um checkpoint e vincula seus responsáveis."""
        if corrida not in self.__aplicacao.corridas:
            raise CorridaNaoEncontradaError("Corrida não encontrada.")
        if professor not in self.__aplicacao.professores:
            raise ProfessorNaoEncontradoError("Professor não encontrado.")

        for checkpoint in self.__aplicacao.checkpoints:
            if (
                checkpoint.corrida == corrida
                and checkpoint.numero == numero
            ):
                raise CheckpointJaExisteError(
                    "Já existe um checkpoint com esse número nessa corrida."
                )

        checkpoint = Checkpoint(numero, corrida, professor)
        self.__aplicacao.adicionar_checkpoint(checkpoint)
        corrida.adicionar_checkpoint(checkpoint)
        professor.adicionar_checkpoint(checkpoint)
        return checkpoint

    def listar(self) -> tuple[Checkpoint, ...]:
        """Retorna todos os checkpoints cadastrados."""
        return self.__aplicacao.checkpoints

    def buscar(self, indice: int) -> Checkpoint:
        """Busca um checkpoint pelo índice informado."""
        try:
            return self.__aplicacao.checkpoints[indice]
        except IndexError as erro:
            raise CheckpointNaoEncontradoError(
                "Checkpoint inválido."
            ) from erro
