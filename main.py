from aplicacao import Trekking
from interface.menus.menu_principal import MenuPrincipal
from servicos import ServicosTrekking


def main() -> None:
    """Inicializa a aplicação, os serviços e a interface."""
    aplicacao = Trekking()
    servicos = ServicosTrekking(aplicacao)

    menu = MenuPrincipal(servicos)
    menu.executar()


if __name__ == "__main__":
    main()
