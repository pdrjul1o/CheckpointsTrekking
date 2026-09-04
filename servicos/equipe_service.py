from aplicacao import Trekking
from excecoes import (
    CorridaNaoEncontradaError,
    EquipeJaExisteError,
    EquipeNaoEncontradaError,
)
from modelos import Corrida, Equipe


class EquipeService:
    """Coordena operações relacionadas às equipes."""

    def __init__(self, aplicacao: Trekking) -> None:
        """Inicializa o serviço com a aplicação que mantém os dados."""
        self.__aplicacao = aplicacao

    def cadastrar(self, nome: str) -> Equipe:
        """Cadastra e retorna uma equipe após validar seu nome."""
        nome = nome.strip()
        if not nome:
            raise ValueError("O nome da equipe não pode ser vazio.")

        for equipe in self.__aplicacao.equipes:
            if equipe.nome.lower() == nome.lower():
                raise EquipeJaExisteError(
                    "Já existe uma equipe com esse nome."
                )

        equipe = Equipe(nome)
        self.__aplicacao.adicionar_equipe(equipe)
        return equipe

    def listar(self) -> tuple[Equipe, ...]:
        """Retorna todas as equipes cadastradas."""
        return self.__aplicacao.equipes

    def buscar(self, indice: int) -> Equipe:
        """Busca uma equipe pelo índice informado."""
        try:
            return self.__aplicacao.equipes[indice]
        except IndexError as erro:
            raise EquipeNaoEncontradaError("Equipe inválida.") from erro

    def adicionar_a_corrida(self, equipe: Equipe, corrida: Corrida) -> None:
        """Registra a participação de uma equipe em uma corrida."""
        if equipe not in self.__aplicacao.equipes:
            raise EquipeNaoEncontradaError("Equipe não encontrada.")
        if corrida not in self.__aplicacao.corridas:
            raise CorridaNaoEncontradaError("Corrida não encontrada.")

        if equipe not in corrida.equipes:
            corrida.adicionar_equipe(equipe)
        if corrida not in equipe.corridas:
            equipe.adicionar_corrida(corrida)
