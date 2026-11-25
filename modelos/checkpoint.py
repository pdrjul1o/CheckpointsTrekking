from sqlalchemy import String, ForeignKey, UniqueConstraint, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base, participacao
from typing import TYPE_CHECKING

from modelos.corrida import Corrida
from modelos.professor import Professor

if TYPE_CHECKING:
    from modelos.passagem import Passagem


class Checkpoint(Base):
    """Representa um checkpoint de uma corrida."""

    __tablename__ = "checkpoint"
    __table_args__ = (UniqueConstraint("id_corrida", "numero"),)
    id: Mapped[int] = mapped_column(primary_key=True)
    _numero: Mapped[int] = mapped_column("numero")
    id_corrida: Mapped[int] = mapped_column(ForeignKey("corrida.id"))
    id_professor: Mapped[int] = mapped_column(ForeignKey("professor.id"))
    _corrida: Mapped["Corrida"] = relationship(back_populates="_checkpoints")
    _professor: Mapped["Professor"] = relationship(back_populates="_checkpoints")
    _passagens: Mapped[list["Passagem"]] = relationship(back_populates="_checkpoint")

    def __init__(
        self,
        numero: int,
        corrida: Corrida,
        professor: Professor,
    ) -> None:
        self._numero: int = numero
        self._corrida: Corrida = corrida
        self._professor: Professor = professor

    @property
    def numero(self) -> int:
        """Retorna o número do checkpoint."""
        return self._numero

    @property
    def corrida(self) -> Corrida:
        """Retorna a corrida à qual o checkpoint pertence."""
        return self._corrida

    @property
    def professor(self) -> Professor:
        """Retorna o professor responsável."""
        return self._professor

    @property
    def passagens(self) -> tuple["Passagem", ...]:
        """Retorna as passagens registradas."""
        return tuple(self._passagens)

    def adicionar_passagem(self, passagem: "Passagem") -> None:
        """Adiciona uma passagem ao checkpoint."""
        if passagem not in self._passagens:
            self._passagens.append(passagem)

    def __str__(self) -> str:
        return f"Checkpoint {self.numero}"
