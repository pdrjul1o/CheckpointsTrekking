class Corrida:
    """
    Representa uma corrida de trekking.
    """

    def __init__(self, nome: str) -> None:
        self.__nome = nome
        self.__checkpoints = []
        self.__passagens = []
        self.__equipes = []

    @property
    def nome(self) -> str:
        """
        Retorna o nome da corrida.
        """
        return self.__nome

    @property
    def checkpoints(self):
        """
        Retorna os checkpoints da corrida.
        """
        return self.__checkpoints

    @property
    def passagens(self):
        """
        Retorna as passagens da corrida.
        """
        return self.__passagens

    @property
    def equipes(self):
        """
        Retorna as equipes da corrida.
        """
        return self.__equipes

    def adicionar_checkpoint(self, checkpoint) -> None:
        """
        Adiciona um checkpoint à corrida.
        """
        self.__checkpoints.append(checkpoint)

    def adicionar_passagem(self, passagem) -> None:
        """
        Adiciona uma passagem à corrida.
        """
        self.__passagens.append(passagem)

    def adicionar_equipe(self, equipe) -> None:
        """
        Adiciona uma equipe à corrida.
        """
        self.__equipes.append(equipe)

    def __str__(self) -> str:
        return self.nome