from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from modelos.checkpoint import Checkpoint
    from modelos.equipe import Equipe
    from modelos.passagem import Passagem


class Corrida:
    """Representa uma corrida de trekking."""

    def __init__(self, nome: str) -> None:
        self.__nome: str = nome
        self.__checkpoints: list["Checkpoint"] = []
        self.__passagens: list["Passagem"] = []
        self.__equipes: list["Equipe"] = []

    @property
    def nome(self) -> str:
        """Retorna o nome da corrida."""
        return self.__nome

    @property
    def checkpoints(self) -> tuple["Checkpoint", ...]:
        """Retorna os checkpoints da corrida."""
        return tuple(self.__checkpoints)

    @property
    def passagens(self) -> tuple["Passagem", ...]:
        """Retorna as passagens da corrida."""
        return tuple(self.__passagens)

    @property
    def equipes(self) -> tuple["Equipe", ...]:
        """Retorna as equipes participantes."""
        return tuple(self.__equipes)

    def adicionar_checkpoint(self, checkpoint: "Checkpoint") -> None:
        """Adiciona um checkpoint à corrida."""
        self.__checkpoints.append(checkpoint)

    def adicionar_passagem(self, passagem: "Passagem") -> None:
        """Adiciona uma passagem à corrida."""
        self.__passagens.append(passagem)

    def adicionar_equipe(self, equipe: "Equipe") -> None:
        """Adiciona uma equipe à corrida."""
        self.__equipes.append(equipe)

    def __str__(self) -> str:
        return self.nome
