from sqlalchemy import String, ForeignKey, UniqueConstraint, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base, participacao
from modelos.checkpoint import Checkpoint
from modelos.corrida import Corrida
from modelos.equipe import Equipe
from modelos.professor import Professor


class Passagem(Base):
    """Representa o registro da passagem de uma equipe."""

    __tablename__ = "passagem"
    __table_args__ = (UniqueConstraint("id_corrida", "id_equipe", "id_checkpoint"),)
    id: Mapped[int] = mapped_column(primary_key=True)
    id_corrida: Mapped[int] = mapped_column(ForeignKey("corrida.id"))
    id_equipe: Mapped[int] = mapped_column(ForeignKey("equipe.id"))
    id_checkpoint: Mapped[int] = mapped_column(ForeignKey("checkpoint.id"))
    id_professor: Mapped[int] = mapped_column(ForeignKey("professor.id"))
    _corrida: Mapped["Corrida"] = relationship(back_populates="_passagens")
    _equipe: Mapped["Equipe"] = relationship(back_populates="_passagens")
    _checkpoint: Mapped["Checkpoint"] = relationship(back_populates="_passagens")
    _professor: Mapped["Professor"] = relationship(back_populates="_passagens")
    _momento: Mapped[str] = mapped_column("momento")

    def __init__(
        self,
        corrida: Corrida,
        equipe: Equipe,
        checkpoint: Checkpoint,
        professor: Professor,
        momento: str,
    ) -> None:
        self._corrida: Corrida = corrida
        self._equipe: Equipe = equipe
        self._checkpoint: Checkpoint = checkpoint
        self._professor: Professor = professor
        self._momento: str = momento

    @property
    def corrida(self) -> Corrida:
        """Retorna a corrida da passagem."""
        return self._corrida

    @property
    def equipe(self) -> Equipe:
        """Retorna a equipe da passagem."""
        return self._equipe

    @property
    def checkpoint(self) -> Checkpoint:
        """Retorna o checkpoint da passagem."""
        return self._checkpoint

    @property
    def professor(self) -> Professor:
        """Retorna o professor responsável pelo registro."""
        return self._professor

    @property
    def momento(self) -> str:
        """Retorna o momento da passagem."""
        return self._momento

    def __str__(self) -> str:
        return (
            f"{self.equipe.nome} - "
            f"Checkpoint {self.checkpoint.numero} - "
            f"{self.momento}"
        )
