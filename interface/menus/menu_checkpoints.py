from interface.menu import Menu
from interface.telas.tela_checkpoints import TelaCheckpoints


class MenuCheckpoints(Menu):
    """
    Menu de operações relacionadas aos checkpoints.
    """

    def executar(self) -> None:

        tela = TelaCheckpoints(self._trekking)

        while True:
            print()
            print("=" * 50)
            print("CHECKPOINTS")
            print("=" * 50)
            print("1 - Cadastrar checkpoint")
            print("2 - Listar checkpoints")
            print("3 - Consultar checkpoint")
            print("4 - Consultar professor responsável")
            print("5 - Consultar equipes que passaram")
            print("0 - Voltar")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                tela.cadastrar()

            elif opcao == "2":
                tela.listar()

            elif opcao == "3":
                tela.consultar()

            elif opcao == "4":
                tela.consultar_professor()

            elif opcao == "5":
                tela.listar_equipes()

            elif opcao == "0":
                break

            else:
                print("Opção inválida.")