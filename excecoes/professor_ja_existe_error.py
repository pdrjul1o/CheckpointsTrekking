from .trekking_error import TrekkingError


class ProfessorJaExisteError(TrekkingError):
    """
    Ocorre quando já existe um professor com o mesmo nome.
    """
    pass