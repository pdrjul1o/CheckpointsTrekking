from sqlalchemy import Integer, ForeignKey, Date
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base

class Emprestimo(Base):
    __tablename__ = "emprestimos"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    livro_id: Mapped[int] = mapped_column(ForeignKey("livros.id"))
    usuario_id: Mapped[int] = mapped_column(ForeignKey("usuarios.id"))
    data_emprestimo: Mapped[Date]
    data_devolucao: Mapped[Date]

    livro = relationship("Livro", back_populates="emprestimos")
    usuario = relationship("Usuario", back_populates="emprestimos")
