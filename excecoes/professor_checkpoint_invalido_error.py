from .trekking_error import TrekkingError


class ProfessorCheckpointInvalidoError(TrekkingError):
    """Ocorre quando o professor não é responsável pelo checkpoint."""
    pass
