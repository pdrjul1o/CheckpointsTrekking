from abc import ABC, abstractmethod

from servicos import ServicosTrekking


class Menu(ABC):
    """Classe abstrata que representa um menu da aplicação."""

    def __init__(self, servicos: ServicosTrekking) -> None:
        self._servicos = servicos

    @abstractmethod
    def executar(self) -> None:
        """Executa o menu."""
        pass
