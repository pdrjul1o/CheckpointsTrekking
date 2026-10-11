from .trekking_error import TrekkingError


class CheckpointJaExisteError(TrekkingError):
    """Ocorre quando o número do checkpoint já existe na corrida."""
    pass
