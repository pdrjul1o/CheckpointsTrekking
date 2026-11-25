from sqlalchemy.exc import SQLAlchemyError
from aplicacao import Trekking
from interface.menus.menu_principal import MenuPrincipal
from servicos import ServicosTrekking


def main() -> None:
    """Inicializa a aplicação e encerra a sessão ao sair."""
    try:
        with Trekking() as aplicacao:
            MenuPrincipal(ServicosTrekking(aplicacao)).executar()
    except (SQLAlchemyError, OSError) as erro:
        print(f"Falha de persistência: {erro}")

if __name__ == '__main__':
    main()
