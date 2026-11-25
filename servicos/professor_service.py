from aplicacao import Trekking
from excecoes import ProfessorJaExisteError, ProfessorNaoEncontradoError
from modelos import Professor


class ProfessorService:
    """Coordena operações relacionadas aos professores."""

    def __init__(self, aplicacao: Trekking) -> None:
        """Inicializa o serviço com a aplicação que mantém os dados."""
        self.__aplicacao = aplicacao

    def cadastrar(self, nome: str) -> Professor:
        """Cadastra e retorna um professor após validar seu nome."""
        nome = nome.strip()
        if not nome:
            raise ValueError("O nome do professor não pode ser vazio.")

        for professor in self.__aplicacao.professores:
            if professor.nome.lower() == nome.lower():
                raise ProfessorJaExisteError(
                    "Já existe um professor com esse nome."
                )

        professor = Professor(nome)
        self.__aplicacao.adicionar_professor(professor)
        return professor

    def listar(self) -> tuple[Professor, ...]:
        """Retorna todos os professores cadastrados."""
        return self.__aplicacao.professores

    def buscar(self, indice: int) -> Professor:
        """Busca um professor pelo índice informado."""
        try:
            if indice < 0:
                raise IndexError(indice)
            return self.__aplicacao.professores[indice]
        except IndexError as erro:
            raise ProfessorNaoEncontradoError(
                "Professor inválido."
            ) from erro

    def atualizar(self, indice: int, nome: str) -> Professor:
        """Atualiza o nome de um registro, mantendo a unicidade."""
        objeto = self.buscar(indice)
        nome = nome.strip()
        if not nome:
            raise ValueError("O nome não pode ser vazio.")
        if any(x is not objeto and x.nome.lower() == nome.lower() for x in self.listar()):
            raise ProfessorJaExisteError("Já existe um registro com esse nome.")
        objeto.renomear(nome)
        self.__aplicacao.salvar_dados()
        return objeto

    def remover(self, indice: int) -> None:
        """Exclui somente registros sem dependências no sistema."""
        objeto = self.buscar(indice)
        if objeto.checkpoints or objeto.passagens:
            raise ValueError("Não é possível remover um registro com vínculos.")
        self.__aplicacao.remover(objeto)
