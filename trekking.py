from modelos import (
    Corrida,
    Equipe,
    Professor,
    Checkpoint,
    Passagem
)

from excecoes import (
    CorridaJaExisteError,
    CorridaNaoEncontradaError,
    EquipeJaExisteError,
    EquipeNaoEncontradaError,
    ProfessorJaExisteError,
    ProfessorNaoEncontradoError,
    CheckpointNaoEncontradoError,
    EquipeNaoParticipanteError,
    PassagemJaRegistradaError
)


class Trekking:
    """
    Classe principal da aplicação.

    Responsável por manter as coleções em memória
    e coordenar as operações do sistema.
    """

    def __init__(self) -> None:
        self.__corridas: list[Corrida] = []
        self.__equipes: list[Equipe] = []
        self.__professores: list[Professor] = []
        self.__checkpoints: list[Checkpoint] = []
        self.__passagens: list[Passagem] = []

    # ======================================================
    # CORRIDAS
    # ======================================================

    def cadastrar_corrida(self, nome: str) -> Corrida:
        """
        Cadastra uma nova corrida.
        """

        nome = nome.strip()

        if not nome:
            raise ValueError(
                "O nome da corrida não pode ser vazio."
            )

        for corrida in self.__corridas:
            if corrida.nome.lower() == nome.lower():
                raise CorridaJaExisteError(
                    "Já existe uma corrida com esse nome."
                )

        corrida = Corrida(nome)

        self.__corridas.append(corrida)

        return corrida

    def listar_corridas(self) -> list[Corrida]:
        """
        Retorna todas as corridas cadastradas.
        """
        return self.__corridas

    def buscar_corrida(self, indice: int) -> Corrida:
        """
        Busca uma corrida pelo índice.
        """

        try:
            return self.__corridas[indice]

        except IndexError:
            raise CorridaNaoEncontradaError(
                "Corrida inválida."
            )

    # ======================================================
    # EQUIPES
    # ======================================================

    def cadastrar_equipe(self, nome: str) -> Equipe:
        """
        Cadastra uma nova equipe.
        """

        nome = nome.strip()

        if not nome:
            raise ValueError(
                "O nome da equipe não pode ser vazio."
            )

        for equipe in self.__equipes:
            if equipe.nome.lower() == nome.lower():
                raise EquipeJaExisteError(
                    "Já existe uma equipe com esse nome."
                )

        equipe = Equipe(nome)

        self.__equipes.append(equipe)

        return equipe

    def listar_equipes(self) -> list[Equipe]:
        """
        Retorna todas as equipes cadastradas.
        """
        return self.__equipes

    def buscar_equipe(self, indice: int) -> Equipe:
        """
        Busca uma equipe pelo índice.
        """

        try:
            return self.__equipes[indice]

        except IndexError:
            raise EquipeNaoEncontradaError(
                "Equipe inválida."
            )

    # ======================================================
    # PROFESSORES
    # ======================================================

    def cadastrar_professor(self, nome: str) -> Professor:
        """
        Cadastra um novo professor.
        """

        nome = nome.strip()

        if not nome:
            raise ValueError(
                "O nome do professor não pode ser vazio."
            )

        for professor in self.__professores:
            if professor.nome.lower() == nome.lower():
                raise ProfessorJaExisteError(
                    "Já existe um professor com esse nome."
                )

        professor = Professor(nome)

        self.__professores.append(professor)

        return professor

    def listar_professores(self) -> list[Professor]:
        """
        Retorna todos os professores cadastrados.
        """
        return self.__professores

    def buscar_professor(self, indice: int) -> Professor:
        """
        Busca um professor pelo índice.
        """

        try:
            return self.__professores[indice]

        except IndexError:
            raise ProfessorNaoEncontradoError(
                "Professor inválido."
            )

    # ======================================================
    # CHECKPOINTS
    # ======================================================

    def cadastrar_checkpoint(
        self,
        numero: int,
        corrida: Corrida,
        professor: Professor
    ) -> Checkpoint:
        """
        Cadastra um checkpoint em uma corrida.
        """

        for checkpoint in self.__checkpoints:

            if (
                checkpoint.corrida == corrida
                and checkpoint.numero == numero
            ):
                raise ValueError(
                    "Já existe um checkpoint com esse número nessa corrida."
                )

        checkpoint = Checkpoint(
            numero,
            corrida,
            professor
        )

        self.__checkpoints.append(checkpoint)

        corrida.adicionar_checkpoint(checkpoint)

        professor.adicionar_checkpoint(checkpoint)

        return checkpoint

    def listar_checkpoints(self) -> list[Checkpoint]:
        """
        Retorna todos os checkpoints cadastrados.
        """
        return self.__checkpoints

    def buscar_checkpoint(self, indice: int) -> Checkpoint:
        """
        Busca um checkpoint pelo índice.
        """

        try:
            return self.__checkpoints[indice]

        except IndexError:
            raise CheckpointNaoEncontradoError(
                "Checkpoint inválido."
            )

    # ======================================================
    # PARTICIPAÇÃO
    # ======================================================

    def adicionar_equipe_corrida(
        self,
        equipe: Equipe,
        corrida: Corrida
    ) -> None:
        """
        Adiciona uma equipe como participante de uma corrida.
        """

        if equipe not in self.__equipes:
            raise EquipeNaoEncontradaError(
                "Equipe não encontrada."
            )

        if corrida not in self.__corridas:
            raise CorridaNaoEncontradaError(
                "Corrida não encontrada."
            )

        if equipe not in corrida.equipes:
            corrida.adicionar_equipe(equipe)

        if corrida not in equipe.corridas:
            equipe.adicionar_corrida(corrida)

    # ======================================================
    # PASSAGENS
    # ======================================================

    def registrar_passagem(
        self,
        corrida: Corrida,
        equipe: Equipe,
        checkpoint: Checkpoint,
        professor: Professor,
        momento: str
    ) -> Passagem:
        """
        Registra a passagem de uma equipe por um checkpoint.
        """

        if corrida not in self.__corridas:
            raise CorridaNaoEncontradaError(
                "Corrida não encontrada."
            )

        if equipe not in self.__equipes:
            raise EquipeNaoEncontradaError(
                "Equipe não encontrada."
            )

        if checkpoint not in self.__checkpoints:
            raise CheckpointNaoEncontradoError(
                "Checkpoint não encontrado."
            )

        if professor not in self.__professores:
            raise ProfessorNaoEncontradoError(
                "Professor não encontrado."
            )

        if checkpoint.corrida != corrida:
            raise ValueError(
                "O checkpoint não pertence a essa corrida."
            )

        if checkpoint.professor != professor:
            raise ValueError(
                "O professor não é responsável por esse checkpoint."
            )

        if corrida not in equipe.corridas:
            raise EquipeNaoParticipanteError(
                "A equipe não participa dessa corrida."
            )

        for passagem in self.__passagens:

            if (
                passagem.corrida == corrida
                and passagem.equipe == equipe
                and passagem.checkpoint == checkpoint
            ):
                raise PassagemJaRegistradaError(
                    "Essa equipe já passou por esse checkpoint."
                )

        passagem = Passagem(
            corrida,
            equipe,
            checkpoint,
            professor,
            momento
        )

        self.__passagens.append(passagem)

        corrida.adicionar_passagem(passagem)
        equipe.adicionar_passagem(passagem)
        checkpoint.adicionar_passagem(passagem)

        return passagem

    def listar_passagens(self) -> list[Passagem]:
        """
        Retorna todas as passagens registradas.
        """
        return self.__passagens

    def listar_passagens_corrida(
        self,
        corrida: Corrida
    ) -> list[Passagem]:
        """
        Retorna as passagens de uma corrida.
        """

        return [
            passagem
            for passagem in self.__passagens
            if passagem.corrida == corrida
        ]

    def listar_passagens_equipe(
        self,
        equipe: Equipe
    ) -> list[Passagem]:
        """
        Retorna as passagens de uma equipe.
        """

        return [
            passagem
            for passagem in self.__passagens
            if passagem.equipe == equipe
        ]

    def listar_passagens_checkpoint(
        self,
        checkpoint: Checkpoint
    ) -> list[Passagem]:
        """
        Retorna as passagens de um checkpoint.
        """

        return [
            passagem
            for passagem in self.__passagens
            if passagem.checkpoint == checkpoint
        ]