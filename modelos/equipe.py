from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from modelos.corrida import Corrida
    from modelos.passagem import Passagem


class Equipe:
    """Representa uma equipe participante de uma corrida."""

    def __init__(self, nome: str) -> None:
        self.__nome: str = nome
        self.__corridas: list["Corrida"] = []
        self.__passagens: list["Passagem"] = []

    @property
    def nome(self) -> str:
        """Retorna o nome da equipe."""
        return self.__nome

    @property
    def corridas(self) -> tuple["Corrida", ...]:
        """Retorna as corridas das quais a equipe participa."""
        return tuple(self.__corridas)

    @property
    def passagens(self) -> tuple["Passagem", ...]:
        """Retorna o histórico de passagens da equipe."""
        return tuple(self.__passagens)

    def adicionar_corrida(self, corrida: "Corrida") -> None:
        """Adiciona uma corrida à equipe."""
        self.__corridas.append(corrida)

    def adicionar_passagem(self, passagem: "Passagem") -> None:
        """Adiciona uma passagem ao histórico da equipe."""
        self.__passagens.append(passagem)

    def __str__(self) -> str:
        return self.nome
