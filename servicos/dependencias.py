from aplicacao import Trekking
from .checkpoint_service import CheckpointService
from .corrida_service import CorridaService
from .equipe_service import EquipeService
from .passagem_service import PassagemService
from .professor_service import ProfessorService


class ServicosTrekking:
    """Agrupa as instâncias dos serviços usadas pela interface."""

    def __init__(self, aplicacao: Trekking) -> None:
        """Cria todos os serviços usando a mesma aplicação."""
        self.corridas = CorridaService(aplicacao)
        self.equipes = EquipeService(aplicacao)
        self.professores = ProfessorService(aplicacao)
        self.checkpoints = CheckpointService(aplicacao)
        self.passagens = PassagemService(aplicacao)
