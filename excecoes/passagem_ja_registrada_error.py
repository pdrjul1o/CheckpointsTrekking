from .trekking_error import TrekkingError


class PassagemJaRegistradaError(TrekkingError):
    """
    Ocorre quando uma equipe já possui uma passagem
    registrada no mesmo checkpoint da mesma corrida.
    """
    pass