from aplicacao import Trekking
from persistencia import ErroPersistencia
from interface.menus.menu_principal import MenuPrincipal
from servicos import ServicosTrekking


def main() -> None:
    """Inicializa a aplicação, os serviços e a interface."""
    try:
        aplicacao = Trekking()
    except (ErroPersistencia, OSError) as erro:
        print(f"Não foi possível carregar os dados: {erro}")
        return
    servicos = ServicosTrekking(aplicacao)

    menu = MenuPrincipal(servicos)
    menu.executar()


if __name__ == "__main__":
    main()
