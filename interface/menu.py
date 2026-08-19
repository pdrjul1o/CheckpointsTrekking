from abc import ABC, abstractmethod

from trekking import Trekking


class Menu(ABC):
    """
    Classe abstrata que representa um menu da aplicação.
    """

    def __init__(self, trekking: Trekking) -> None:
        self._trekking = trekking

    @abstractmethod
    def executar(self) -> None:
        """
        Executa o menu.
        """
        pass