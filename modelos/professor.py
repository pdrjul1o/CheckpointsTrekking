class Professor:
    """
    Representa um professor responsável por checkpoints.
    """

    def __init__(self, nome: str) -> None:
        self.__nome = nome
        self.__checkpoints = []

    @property
    def nome(self) -> str:
        """
        Retorna o nome do professor.
        """
        return self.__nome

    @property
    def checkpoints(self):
        """
        Retorna os checkpoints pelos quais o professor é responsável.
        """
        return self.__checkpoints

    def adicionar_checkpoint(self, checkpoint) -> None:
        """
        Adiciona um checkpoint à responsabilidade do professor.
        """
        self.__checkpoints.append(checkpoint)

    def __str__(self) -> str:
        return self.nome