class Equipe:
    """
    Representa uma equipe participante de uma corrida.
    """

    def __init__(self, nome: str) -> None:
        self.__nome = nome
        self.__corridas = []
        self.__passagens = []

    @property
    def nome(self) -> str:
        """
        Retorna o nome da equipe.
        """
        return self.__nome

    @property
    def corridas(self):
        """
        Retorna as corridas das quais a equipe participa.
        """
        return self.__corridas

    @property
    def passagens(self):
        """
        Retorna as passagens da equipe.
        """
        return self.__passagens

    def adicionar_corrida(self, corrida) -> None:
        """
        Adiciona uma corrida à equipe.
        """
        self.__corridas.append(corrida)

    def adicionar_passagem(self, passagem) -> None:
        """
        Adiciona uma passagem ao histórico da equipe.
        """
        self.__passagens.append(passagem)

    def __str__(self) -> str:
        return self.nome