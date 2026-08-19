from .trekking_error import TrekkingError


class CorridaJaExisteError(TrekkingError):
    """
    Ocorre quando já existe uma corrida com o mesmo nome.
    """
    pass