from trekking import Trekking
from interface.menus.menu_principal import MenuPrincipal


def main() -> None:
    """
    Inicia a aplicação.
    """

    trekking = Trekking()

    menu = MenuPrincipal(trekking)

    menu.executar()


if __name__ == "__main__":
    main()