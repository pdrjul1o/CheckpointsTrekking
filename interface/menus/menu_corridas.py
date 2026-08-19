from interface.menu import Menu
from interface.telas.tela_corridas import TelaCorridas


class MenuCorridas(Menu):
    """
    Menu de operações relacionadas às corridas.
    """

    def executar(self) -> None:

        tela = TelaCorridas(self._trekking)

        while True:
            print()
            print("=" * 50)
            print("CORRIDAS")
            print("=" * 50)
            print("1 - Cadastrar corrida")
            print("2 - Listar corridas")
            print("3 - Consultar corrida")
            print("4 - Consultar checkpoints da corrida")
            print("5 - Consultar passagens da corrida")
            print("0 - Voltar")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                tela.cadastrar()

            elif opcao == "2":
                tela.listar()

            elif opcao == "3":
                tela.consultar()

            elif opcao == "4":
                tela.listar_checkpoints()

            elif opcao == "5":
                tela.listar_passagens()

            elif opcao == "0":
                break

            else:
                print("Opção inválida.")