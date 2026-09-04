from aplicacao import Trekking
from excecoes import EquipeNaoParticipanteError, PassagemJaRegistradaError
from servicos import ServicosTrekking


def testar_fluxo_completo() -> None:
    """Executa um fluxo válido completo do estudo de caso."""
    aplicacao = Trekking()
    servicos = ServicosTrekking(aplicacao)

    corrida = servicos.corridas.cadastrar("Trilha IFRN")
    equipe = servicos.equipes.cadastrar("Equipe A")
    professor = servicos.professores.cadastrar("Professor Carlos")
    checkpoint = servicos.checkpoints.cadastrar(1, corrida, professor)

    servicos.equipes.adicionar_a_corrida(equipe, corrida)
    passagem = servicos.passagens.registrar(
        corrida,
        equipe,
        checkpoint,
        professor,
        "09:42",
    )

    assert passagem in servicos.passagens.listar()
    assert checkpoint in corrida.checkpoints
    assert passagem in servicos.passagens.listar_por_corrida(corrida)
    assert passagem in servicos.passagens.listar_por_equipe(equipe)
    assert passagem in servicos.passagens.listar_por_checkpoint(checkpoint)


def testar_situacao_invalida() -> None:
    """Verifica a exceção ao registrar a mesma passagem duas vezes."""
    aplicacao = Trekking()
    servicos = ServicosTrekking(aplicacao)

    corrida = servicos.corridas.cadastrar("Trilha Teste")
    equipe = servicos.equipes.cadastrar("Equipe Teste")
    professor = servicos.professores.cadastrar("Professor Teste")
    checkpoint = servicos.checkpoints.cadastrar(1, corrida, professor)
    servicos.equipes.adicionar_a_corrida(equipe, corrida)

    servicos.passagens.registrar(
        corrida, equipe, checkpoint, professor, "10:00"
    )

    try:
        servicos.passagens.registrar(
            corrida, equipe, checkpoint, professor, "10:05"
        )
    except PassagemJaRegistradaError:
        pass
    else:
        raise AssertionError("A segunda passagem deveria gerar exceção.")

    equipe2 = servicos.equipes.cadastrar("Equipe Fora")
    try:
        servicos.passagens.registrar(
            corrida, equipe2, checkpoint, professor, "10:10"
        )
    except EquipeNaoParticipanteError:
        pass
    else:
        raise AssertionError("Equipe sem participação deveria gerar exceção.")


if __name__ == "__main__":
    testar_fluxo_completo()
    testar_situacao_invalida()
    print("Testes da segunda versão executados com sucesso.")
