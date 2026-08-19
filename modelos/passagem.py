from modelos.corrida import Corrida
from modelos.equipe import Equipe
from modelos.checkpoint import Checkpoint
from modelos.professor import Professor


class Passagem:
    """
    Representa o registro da passagem de uma equipe
    por um checkpoint durante uma corrida.
    """

    def __init__(
        self,
        corrida: Corrida,
        equipe: Equipe,
        checkpoint: Checkpoint,
        professor: Professor,
        momento: str
    ) -> None:

        self.__corrida = corrida
        self.__equipe = equipe
        self.__checkpoint = checkpoint
        self.__professor = professor
        self.__momento = momento

    @property
    def corrida(self) -> Corrida:
        """
        Retorna a corrida da passagem.
        """
        return self.__corrida

    @property
    def equipe(self) -> Equipe:
        """
        Retorna a equipe da passagem.
        """
        return self.__equipe

    @property
    def checkpoint(self) -> Checkpoint:
        """
        Retorna o checkpoint da passagem.
        """
        return self.__checkpoint

    @property
    def professor(self) -> Professor:
        """
        Retorna o professor responsável pelo registro.
        """
        return self.__professor

    @property
    def momento(self) -> str:
        """
        Retorna o momento da passagem.
        """
        return self.__momento

    def __str__(self) -> str:
        return (
            f"{self.equipe.nome} - "
            f"Checkpoint {self.checkpoint.numero} - "
            f"{self.momento}"
        )