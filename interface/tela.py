from abc import ABC, abstractmethod

from trekking import Trekking


class Tela(ABC):
    """
    Classe abstrata que representa uma tela da aplicação.
    """

    def __init__(self, trekking: Trekking) -> None:
        self._trekking = trekking

    def mostrar_titulo(self, titulo: str) -> None:
        """
        Exibe o título de uma tela.
        """
        print()
        print("=" * 50)
        print(titulo)
        print("=" * 50)

    @abstractmethod
    def exibir(self) -> None:
        """
        Exibe a tela.
        """
        pass