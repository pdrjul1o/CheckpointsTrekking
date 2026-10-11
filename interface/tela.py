from abc import ABC, abstractmethod

from servicos import ServicosTrekking


class Tela(ABC):
    """Classe abstrata que representa uma tela da aplicação."""

    def __init__(self, servicos: ServicosTrekking) -> None:
        self._servicos = servicos

    def mostrar_titulo(self, titulo: str) -> None:
        """Exibe o título de uma tela."""
        print()
        print("=" * 50)
        print(titulo)
        print("=" * 50)

    @abstractmethod
    def exibir(self) -> None:
        """Exibe a tela."""
        pass
