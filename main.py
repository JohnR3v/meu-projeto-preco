from database import conectar
from menu import menu_principal


def main():
    conn = conectar()
    menu_principal(conn)
    conn.close()


if __name__ == "__main__":
    main()
