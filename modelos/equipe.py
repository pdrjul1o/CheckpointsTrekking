from sqlalchemy import String, ForeignKey, UniqueConstraint, CheckConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base, participacao
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from modelos.corrida import Corrida
    from modelos.passagem import Passagem


class Equipe(Base):
    """Representa uma equipe participante de uma corrida."""

    __tablename__ = "equipe"
    id: Mapped[int] = mapped_column(primary_key=True)
    _nome: Mapped[str] = mapped_column("nome", String(120, collation="NOCASE"), unique=True)
    _corridas: Mapped[list["Corrida"]] = relationship(secondary=participacao, back_populates="_equipes")
    _passagens: Mapped[list["Passagem"]] = relationship(back_populates="_equipe")

    def __init__(self, nome: str) -> None:
        self._nome: str = nome

    @property
    def nome(self) -> str:
        """Retorna o nome da equipe."""
        return self._nome

    @property
    def corridas(self) -> tuple["Corrida", ...]:
        """Retorna as corridas das quais a equipe participa."""
        return tuple(self._corridas)

    @property
    def passagens(self) -> tuple["Passagem", ...]:
        """Retorna o histórico de passagens da equipe."""
        return tuple(self._passagens)

    def adicionar_corrida(self, corrida: "Corrida") -> None:
        """Adiciona uma corrida à equipe."""
        if corrida not in self._corridas:
            self._corridas.append(corrida)

    def adicionar_passagem(self, passagem: "Passagem") -> None:
        """Adiciona uma passagem ao histórico da equipe."""
        if passagem not in self._passagens:
            self._passagens.append(passagem)

    def __str__(self) -> str:
        return self.nome

    def renomear(self, nome: str) -> None:
        """Altera o nome após validação pelo serviço."""
        self._nome = nome
