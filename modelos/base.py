from sqlalchemy import Column, ForeignKey, Table
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    """Base comum dos modelos ORM."""

participacao = Table(
    "participacao", Base.metadata,
    Column("id_corrida", ForeignKey("corrida.id"), primary_key=True),
    Column("id_equipe", ForeignKey("equipe.id"), primary_key=True),
)
