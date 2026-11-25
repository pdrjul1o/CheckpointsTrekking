from pathlib import Path
from sqlalchemy import create_engine, event
from sqlalchemy.engine import Engine, URL
from sqlalchemy.orm import Session, sessionmaker
from modelos.base import Base
import modelos


def configurar_banco(diretorio: Path) -> tuple[Engine, sessionmaker[Session]]:
    """Cria o banco SQLite e disponibiliza uma fábrica de sessões."""
    diretorio.mkdir(parents=True, exist_ok=True)
    engine = create_engine(URL.create('sqlite', database=str(diretorio / 'trekking.db')))

    @event.listens_for(engine, 'connect')
    def ativar_chaves_estrangeiras(conexao, _registro):
        conexao.execute('PRAGMA foreign_keys=ON')

    Base.metadata.create_all(engine)
    return engine, sessionmaker(bind=engine, expire_on_commit=False)
