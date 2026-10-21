from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from modelos.checkpoint import Checkpoint
    from modelos.equipe import Equipe
    from modelos.passagem import Passagem


class Corrida:
    """Representa uma corrida de trekking."""

    def __init__(self, nome: str, total_checkpoints_previstos: int = 1) -> None:
        if type(total_checkpoints_previstos) is not int or total_checkpoints_previstos <= 0:
            raise ValueError("O total de checkpoints previstos deve ser um número inteiro positivo.")
        self.__nome: str = nome
        self.__total_checkpoints_previstos = total_checkpoints_previstos
        self.__checkpoints: list["Checkpoint"] = []
        self.__passagens: list["Passagem"] = []
        self.__equipes: list["Equipe"] = []

    @property
    def nome(self) -> str:
        """Retorna o nome da corrida."""
        return self.__nome

    @property
    def total_checkpoints_previstos(self) -> int:
        """Total planejado e informado no cadastro da corrida."""
        return self.__total_checkpoints_previstos

    @property
    def checkpoints_com_professores(self) -> tuple["Checkpoint", ...]:
        """Checkpoints desta corrida com professor responsável atribuído."""
        return tuple(c for c in self.__checkpoints if c.professor is not None)

    @property
    def total_checkpoints_com_professores(self) -> int:
        return len(self.checkpoints_com_professores)

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
