from sqlalchemy.orm import Session


def confirmar(sessao: Session) -> None:
    """Confirma a transação ou desfaz alterações em caso de falha."""
    try:
        sessao.commit()
    except Exception:
        sessao.rollback()
        raise
