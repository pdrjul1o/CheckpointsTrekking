from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from modelos.checkpoint import Checkpoint


class Professor:
    """Representa um professor responsável por checkpoints."""

    def __init__(self, nome: str) -> None:
        self.__nome: str = nome
        self.__checkpoints: list["Checkpoint"] = []

    @property
    def nome(self) -> str:
        """Retorna o nome do professor."""
        return self.__nome

    @property
    def checkpoints(self) -> tuple["Checkpoint", ...]:
        """Retorna os checkpoints pelos quais é responsável."""
        return tuple(self.__checkpoints)

    def adicionar_checkpoint(self, checkpoint: "Checkpoint") -> None:
        """Adiciona um checkpoint à responsabilidade do professor."""
        self.__checkpoints.append(checkpoint)

    def __str__(self) -> str:
        return self.nome
