from pathlib import Path
from typing import TypeVar
from sqlalchemy import select
from modelos import Corrida, Equipe, Professor, Checkpoint, Passagem
from modelos.base import Base
from persistencia import configurar_banco, confirmar

T = TypeVar('T', bound=Base)

class Trekking:
    """Centraliza o acesso ORM; os serviços conservam as regras de negócio."""

    def __init__(self, diretorio_dados: Path | None = None) -> None:
        self.__engine, fabrica = configurar_banco(diretorio_dados or Path(__file__).resolve().parent / 'dados')
        self.__sessao = fabrica()

    def __enter__(self) -> 'Trekking':
        return self

    def __exit__(self, tipo, erro, traceback) -> None:
        self.close()

    def close(self) -> None:
        """Libera a sessão e as conexões ao encerrar a aplicação."""
        self.__sessao.close()
        self.__engine.dispose()

    def salvar_dados(self) -> None:
        """Confirma alterações feitas nos objetos mapeados."""
        confirmar(self.__sessao)

    def listar(self, modelo: type[T]) -> tuple[T, ...]:
        """Consulta objetos no banco em ordem de identificação."""
        return tuple(self.__sessao.scalars(select(modelo).order_by(modelo.id)).all())

    def adicionar(self, objeto: Base) -> None:
        """Inclui um objeto e confirma a transação."""
        self.__sessao.add(objeto)
        self.salvar_dados()

    def remover(self, objeto: Base) -> None:
        """Remove um objeto previamente validado pelo serviço."""
        self.__sessao.delete(objeto)
        self.salvar_dados()

    def filtrar_passagens(self, **filtros: int) -> list[Passagem]:
        """Consulta passagens pelas chaves informadas pelo serviço."""
        return list(self.__sessao.scalars(select(Passagem).filter_by(**filtros).order_by(Passagem.id)))

    @property
    def corridas(self) -> tuple[Corrida, ...]:
        """Retorna os registros de corridas."""
        return self.listar(Corrida)

    def adicionar_corrida(self, objeto: Corrida) -> None:
        """Persiste o novo objeto."""
        self.adicionar(objeto)

    @property
    def equipes(self) -> tuple[Equipe, ...]:
        """Retorna os registros de equipes."""
        return self.listar(Equipe)

    def adicionar_equipe(self, objeto: Equipe) -> None:
        """Persiste o novo objeto."""
        self.adicionar(objeto)

    @property
    def professores(self) -> tuple[Professor, ...]:
        """Retorna os registros de professores."""
        return self.listar(Professor)

    def adicionar_professor(self, objeto: Professor) -> None:
        """Persiste o novo objeto."""
        self.adicionar(objeto)

    @property
    def checkpoints(self) -> tuple[Checkpoint, ...]:
        """Retorna os registros de checkpoints."""
        return self.listar(Checkpoint)

    def adicionar_checkpoint(self, objeto: Checkpoint) -> None:
        """Persiste o novo objeto."""
        self.adicionar(objeto)

    @property
    def passagens(self) -> tuple[Passagem, ...]:
        """Retorna os registros de passagens."""
        return self.listar(Passagem)

    def adicionar_passagem(self, objeto: Passagem) -> None:
        """Persiste o novo objeto."""
        self.adicionar(objeto)
