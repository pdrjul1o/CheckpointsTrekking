from pathlib import Path
from persistencia import PersistenciaJSON

from modelos import Corrida, Equipe, Professor, Checkpoint, Passagem


class Trekking:
    """
    Mantém os dados da aplicação em memória.

    A classe não concentra regras de negócio. Os serviços utilizam
    os métodos de acesso e inclusão desta classe para trabalhar com
    as coleções mantidas internamente.
    """

    def __init__(self, diretorio_dados: Path | None = None) -> None:
        self.__corridas: list[Corrida] = []
        self.__equipes: list[Equipe] = []
        self.__professores: list[Professor] = []
        self.__checkpoints: list[Checkpoint] = []
        self.__passagens: list[Passagem] = []
        self.__persistencia = PersistenciaJSON(diretorio_dados or Path(__file__).resolve().parent / "dados")
        self.carregar_dados()

    def carregar_dados(self) -> None:
        """Carrega coleções e reconstrói os relacionamentos salvos."""
        (self.__corridas, self.__equipes, self.__professores,
         self.__checkpoints, self.__passagens) = self.__persistencia.carregar()

    def salvar_dados(self) -> None:
        """Persiste o estado atual, sem expor as listas internas."""
        self.__persistencia.salvar(self.corridas, self.equipes, self.professores,
                                  self.checkpoints, self.passagens)

    @property
    def corridas(self) -> tuple[Corrida, ...]:
        """Retorna as corridas cadastradas sem expor a lista interna."""
        return tuple(self.__corridas)

    @property
    def equipes(self) -> tuple[Equipe, ...]:
        """Retorna as equipes cadastradas sem expor a lista interna."""
        return tuple(self.__equipes)

    @property
    def professores(self) -> tuple[Professor, ...]:
        """Retorna os professores cadastrados sem expor a lista interna."""
        return tuple(self.__professores)

    @property
    def checkpoints(self) -> tuple[Checkpoint, ...]:
        """Retorna os checkpoints cadastrados sem expor a lista interna."""
        return tuple(self.__checkpoints)

    @property
    def passagens(self) -> tuple[Passagem, ...]:
        """Retorna as passagens registradas sem expor a lista interna."""
        return tuple(self.__passagens)

    def adicionar_corrida(self, corrida: Corrida) -> None:
        """Adiciona uma corrida à coleção da aplicação."""
        self.__corridas.append(corrida)
        self.salvar_dados()

    def adicionar_equipe(self, equipe: Equipe) -> None:
        """Adiciona uma equipe à coleção da aplicação."""
        self.__equipes.append(equipe)
        self.salvar_dados()

    def adicionar_professor(self, professor: Professor) -> None:
        """Adiciona um professor à coleção da aplicação."""
        self.__professores.append(professor)

    def adicionar_checkpoint(self, checkpoint: Checkpoint) -> None:
        """Adiciona um checkpoint à coleção da aplicação."""
        self.__checkpoints.append(checkpoint)
        self.salvar_dados()

    def adicionar_passagem(self, passagem: Passagem) -> None:
        """Adiciona uma passagem à coleção da aplicação."""
        self.__passagens.append(passagem)
