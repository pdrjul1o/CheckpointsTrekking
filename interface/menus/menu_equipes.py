from interface.menu import Menu
from interface.telas.tela_equipes import TelaEquipes


class MenuEquipes(Menu):
    """
    Menu de operações relacionadas às equipes.
    """

    def executar(self) -> None:

        tela = TelaEquipes(self._trekking)

        while True:
            print()
            print("=" * 50)
            print("EQUIPES")
            print("=" * 50)
            print("1 - Cadastrar equipe")
            print("2 - Listar equipes")
            print("3 - Consultar equipe")
            print("4 - Adicionar equipe a uma corrida")
            print("5 - Consultar histórico da equipe")
            print("0 - Voltar")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                tela.cadastrar()

            elif opcao == "2":
                tela.listar()

            elif opcao == "3":
                tela.consultar()

            elif opcao == "4":
                tela.adicionar_corrida()

            elif opcao == "5":
                tela.historico()

            elif opcao == "0":
                break

            else:
                print("Opção inválida.")