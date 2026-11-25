from sqlalchemy import String, ForeignKey, UniqueConstraint, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base, participacao
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from modelos.checkpoint import Checkpoint
    from modelos.equipe import Equipe
    from modelos.passagem import Passagem


class Corrida(Base):
    """Representa uma corrida de trekking."""

    __tablename__ = "corrida"
    id: Mapped[int] = mapped_column(primary_key=True)
    _nome: Mapped[str] = mapped_column("nome", String(120, collation="NOCASE"), unique=True)
    _total_checkpoints_previstos: Mapped[int] = mapped_column("total_checkpoints_previstos", CheckConstraint("total_checkpoints_previstos > 0"))
    _checkpoints: Mapped[list["Checkpoint"]] = relationship(back_populates="_corrida")
    _passagens: Mapped[list["Passagem"]] = relationship(back_populates="_corrida")
    _equipes: Mapped[list["Equipe"]] = relationship(secondary=participacao, back_populates="_corridas")

    def __init__(self, nome: str, total_checkpoints_previstos: int = 1) -> None:
        if type(total_checkpoints_previstos) is not int or total_checkpoints_previstos <= 0:
            raise ValueError("O total de checkpoints previstos deve ser um número inteiro positivo.")
        self._nome: str = nome
        self._total_checkpoints_previstos = total_checkpoints_previstos

    @property
    def nome(self) -> str:
        """Retorna o nome da corrida."""
        return self._nome

    @property
    def total_checkpoints_previstos(self) -> int:
        """Total planejado e informado no cadastro da corrida."""
        return self._total_checkpoints_previstos

    @property
    def checkpoints_com_professores(self) -> tuple["Checkpoint", ...]:
        """Checkpoints desta corrida com professor responsável atribuído."""
        return tuple(c for c in self._checkpoints if c.professor is not None)

    @property
    def total_checkpoints_com_professores(self) -> int:
        return len(self.checkpoints_com_professores)

    @property
    def checkpoints(self) -> tuple["Checkpoint", ...]:
        """Retorna os checkpoints da corrida."""
        return tuple(self._checkpoints)

    @property
    def passagens(self) -> tuple["Passagem", ...]:
        """Retorna as passagens da corrida."""
        return tuple(self._passagens)

    @property
    def equipes(self) -> tuple["Equipe", ...]:
        """Retorna as equipes participantes."""
        return tuple(self._equipes)

    def adicionar_checkpoint(self, checkpoint: "Checkpoint") -> None:
        """Adiciona um checkpoint à corrida."""
        if checkpoint not in self._checkpoints:
            self._checkpoints.append(checkpoint)

    def adicionar_passagem(self, passagem: "Passagem") -> None:
        """Adiciona uma passagem à corrida."""
        if passagem not in self._passagens:
            self._passagens.append(passagem)

    def adicionar_equipe(self, equipe: "Equipe") -> None:
        """Adiciona uma equipe à corrida."""
        if equipe not in self._equipes:
            self._equipes.append(equipe)

    def __str__(self) -> str:
        return self.nome

    def renomear(self, nome: str) -> None:
        """Altera o nome após validação pelo serviço."""
        self._nome = nome
