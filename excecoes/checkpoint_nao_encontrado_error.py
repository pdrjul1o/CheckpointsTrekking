from .trekking_error import TrekkingError


class CheckpointNaoEncontradoError(TrekkingError):
    """
    Ocorre quando um checkpoint não é encontrado.
    """
    pass