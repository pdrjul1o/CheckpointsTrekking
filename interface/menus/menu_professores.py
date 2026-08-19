from interface.menu import Menu
from interface.telas.tela_professores import TelaProfessores


class MenuProfessores(Menu):
    """
    Menu de operações relacionadas aos professores.
    """

    def executar(self) -> None:

        tela = TelaProfessores(self._trekking)

        while True:
            print()
            print("=" * 50)
            print("PROFESSORES")
            print("=" * 50)
            print("1 - Cadastrar professor")
            print("2 - Listar professores")
            print("3 - Consultar professor")
            print("4 - Consultar checkpoints do professor")
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

            elif opcao == "0":
                break

            else:
                print("Opção inválida.")