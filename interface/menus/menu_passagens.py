from interface.menu import Menu
from interface.telas.tela_passagens import TelaPassagens


class MenuPassagens(Menu):
    """
    Menu de operações relacionadas às passagens.
    """

    def executar(self) -> None:

        tela = TelaPassagens(self._trekking)

        while True:
            print()
            print("=" * 50)
            print("PASSAGENS")
            print("=" * 50)
            print("1 - Registrar passagem")
            print("2 - Listar passagens")
            print("3 - Listar passagens da corrida")
            print("4 - Consultar progressão da equipe")
            print("5 - Consultar passagens do checkpoint")
            print("6 - Consultar histórico da equipe")
            print("0 - Voltar")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                tela.registrar()

            elif opcao == "2":
                tela.listar()

            elif opcao == "3":
                tela.listar_corrida()

            elif opcao == "4":
                tela.progressao_equipe()

            elif opcao == "5":
                tela.listar_checkpoint()

            elif opcao == "6":
                tela.historico_equipe()

            elif opcao == "0":
                break

            else:
                print("Opção inválida.")