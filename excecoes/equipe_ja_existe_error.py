from .trekking_error import TrekkingError


class EquipeJaExisteError(TrekkingError):
    """
    Ocorre quando já existe uma equipe com o mesmo nome.
    """
    pass