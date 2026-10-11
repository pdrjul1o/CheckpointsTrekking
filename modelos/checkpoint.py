from typing import TYPE_CHECKING

from modelos.corrida import Corrida
from modelos.professor import Professor

if TYPE_CHECKING:
    from modelos.passagem import Passagem


class Checkpoint:
    """Representa um checkpoint de uma corrida."""

    def __init__(
        self,
        numero: int,
        corrida: Corrida,
        professor: Professor,
    ) -> None:
        self.__numero: int = numero
        self.__corrida: Corrida = corrida
        self.__professor: Professor = professor
        self.__passagens: list["Passagem"] = []

    @property
    def numero(self) -> int:
        """Retorna o número do checkpoint."""
        return self.__numero

    @property
    def corrida(self) -> Corrida:
        """Retorna a corrida à qual o checkpoint pertence."""
        return self.__corrida

    @property
    def professor(self) -> Professor:
        """Retorna o professor responsável."""
        return self.__professor

    @property
    def passagens(self) -> tuple["Passagem", ...]:
        """Retorna as passagens registradas."""
        return tuple(self.__passagens)

    def adicionar_passagem(self, passagem: "Passagem") -> None:
        """Adiciona uma passagem ao checkpoint."""
        self.__passagens.append(passagem)

    def __str__(self) -> str:
        return f"Checkpoint {self.numero}"
