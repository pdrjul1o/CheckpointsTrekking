from sqlalchemy import select
from ..persistencia.sessao import get_session
from ..modelos.livro import Livro

def listar_livros():
    with get_session() as session:
        return session.scalars(select(Livro)).all()

def adicionar_livro(titulo, autor):
    with get_session() as session:
        livro = Livro(titulo=titulo, autor=autor)
        session.add(livro)
