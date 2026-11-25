from sqlalchemy import String, ForeignKey, UniqueConstraint, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base, participacao
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from modelos.checkpoint import Checkpoint
    from modelos.passagem import Passagem


class Professor(Base):
    """Representa um professor responsável por checkpoints."""

    __tablename__ = "professor"
    id: Mapped[int] = mapped_column(primary_key=True)
    _nome: Mapped[str] = mapped_column("nome", String(120, collation="NOCASE"), unique=True)
    _checkpoints: Mapped[list["Checkpoint"]] = relationship(back_populates="_professor")
    _passagens: Mapped[list["Passagem"]] = relationship(back_populates="_professor")

    def __init__(self, nome: str) -> None:
        self._nome: str = nome

    @property
    def nome(self) -> str:
        """Retorna o nome do professor."""
        return self._nome

    @property
    def checkpoints(self) -> tuple["Checkpoint", ...]:
        """Retorna os checkpoints pelos quais é responsável."""
        return tuple(self._checkpoints)

    def adicionar_checkpoint(self, checkpoint: "Checkpoint") -> None:
        """Adiciona um checkpoint à responsabilidade do professor."""
        if checkpoint not in self._checkpoints:
            self._checkpoints.append(checkpoint)

    def __str__(self) -> str:
        return self.nome

    def renomear(self, nome: str) -> None:
        """Altera o nome após validação pelo serviço."""
        self._nome = nome

    @property
    def passagens(self) -> tuple["Passagem", ...]:
        """Retorna as passagens registradas pelo professor."""
        return tuple(self._passagens)
