from aplicacao import Trekking
from excecoes import CorridaJaExisteError, CorridaNaoEncontradaError
from modelos import Corrida


class CorridaService:
    """Coordena operações relacionadas às corridas."""

    def __init__(self, aplicacao: Trekking) -> None:
        """Inicializa o serviço com a aplicação que mantém os dados."""
        self.__aplicacao = aplicacao

    def cadastrar(self, nome: str) -> Corrida:
        """Cadastra e retorna uma corrida após validar seu nome."""
        nome = nome.strip()
        if not nome:
            raise ValueError("O nome da corrida não pode ser vazio.")

        for corrida in self.__aplicacao.corridas:
            if corrida.nome.lower() == nome.lower():
                raise CorridaJaExisteError(
                    "Já existe uma corrida com esse nome."
                )

        corrida = Corrida(nome)
        self.__aplicacao.adicionar_corrida(corrida)
        return corrida

    def listar(self) -> tuple[Corrida, ...]:
        """Retorna todas as corridas cadastradas."""
        return self.__aplicacao.corridas

    def buscar(self, indice: int) -> Corrida:
        """Busca uma corrida pelo índice informado."""
        try:
            return self.__aplicacao.corridas[indice]
        except IndexError as erro:
            raise CorridaNaoEncontradaError("Corrida inválida.") from erro
