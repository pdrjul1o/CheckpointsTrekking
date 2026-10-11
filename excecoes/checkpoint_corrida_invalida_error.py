from .trekking_error import TrekkingError


class CheckpointCorridaInvalidaError(TrekkingError):
    """Ocorre quando o checkpoint não pertence à corrida informada."""
    pass
