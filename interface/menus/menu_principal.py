from interface.menu import Menu

from interface.menus.menu_corridas import MenuCorridas
from interface.menus.menu_equipes import MenuEquipes
from interface.menus.menu_professores import MenuProfessores
from interface.menus.menu_checkpoints import MenuCheckpoints
from interface.menus.menu_passagens import MenuPassagens


class MenuPrincipal(Menu):
    """
    Menu principal da aplicação.
    """

    def executar(self) -> None:

        while True:
            print()
            print("=" * 50)
            print("SISTEMA DE TREKKING")
            print("=" * 50)
            print("1 - Corridas")
            print("2 - Equipes")
            print("3 - Professores")
            print("4 - Checkpoints")
            print("5 - Passagens")
            print("0 - Sair")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                MenuCorridas(self._trekking).executar()

            elif opcao == "2":
                MenuEquipes(self._trekking).executar()

            elif opcao == "3":
                MenuProfessores(self._trekking).executar()

            elif opcao == "4":
                MenuCheckpoints(self._trekking).executar()

            elif opcao == "5":
                MenuPassagens(self._trekking).executar()

            elif opcao == "0":
                print("Encerrando o sistema...")
                break

            else:
                print("Opção inválida.")