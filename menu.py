from database import buscar_produto, remover_produto, listar_produtos as listar_banco
from produto import processar_produto


def listar_produtos(conn):
    registros = listar_banco(conn)

    if not registros:
        print("Nenhum produto cadastrado.")
        return

    print(f"\nProdutos cadastrados: {len(registros)}")
    for nome, mercado, preco_atual in registros:
        print(f"- {nome} | {mercado} | R$ {preco_atual:.2f}")
    print("-" * 30)


def adicionar_produtos(conn):
    quantidade_produtos = 0

    while True:
        nome = input("Produto ou 'retornar' para voltar ou 'nao' para sair: ").strip().lower()

        if nome == "retornar":
            print("Retornando ao menu principal...")
            return

        if nome == "nao":
            print(f"Produtos adicionados: {quantidade_produtos}")
            print("Programa encerrado.")
            raise SystemExit

        if not nome:
            print("Nome do produto não pode estar vazio.")
            continue

        mercado = input("Mercado ou 'retornar' para voltar: ").strip().lower()

        if mercado == "retornar":
            print("Retornando ao menu principal...")
            return

        if not mercado:
            print("Nome do mercado não pode estar vazio.")
            continue

        processar_produto(conn, nome, mercado)
        quantidade_produtos += 1


def alterar_produto(conn):
    while True:
        print("\n=== ALTERAR PRODUTO ===")
        print("1 - Ver lista")
        print("2 - Alterar direto")
        print("0 - Voltar")
        escolha = input("Escolha: ").strip()

        if escolha == "0":
            print("Retornando ao menu principal...")
            return

        if escolha == "1":
            listar_produtos(conn)
            continue

        if escolha == "2":
            nome = input("Produto ou 'retornar': ").strip().lower()

            if nome == "retornar":
                print("Retornando ao menu principal...")
                return

            if nome == "nao":
                print("Programa encerrado.")
                raise SystemExit

            mercado = input("Mercado ou 'retornar': ").strip().lower()

            if mercado == "retornar":
                print("Retornando ao menu principal...")
                return

            if mercado == "nao":
                print("Programa encerrado.")
                raise SystemExit

            registro = buscar_produto(conn, nome, mercado)

            if not registro:
                print("Produto não encontrado para esse mercado.")
                continue

            processar_produto(conn, nome, mercado)
            return

        print("Opção inválida.")


def remover_produtos(conn):
    while True:
        nome = input("Produto para remover ou 'retornar': ").strip().lower()

        if nome == "retornar":
            print("Retornando ao menu principal...")
            return

        if nome == "nao":
            print("Programa encerrado.")
            raise SystemExit

        mercado = input("Mercado: ").strip().lower()

        if mercado == "retornar":
            print("Retornando ao menu principal...")
            return

        if mercado == "nao":
            print("Programa encerrado.")
            raise SystemExit

        registro = buscar_produto(conn, nome, mercado)

        if not registro:
            print("Produto não encontrado para esse mercado.")
            continue

        remover_produto(conn, nome, mercado)
        print(f"Produto removido: {nome} | {mercado}")
        return


def menu_principal(conn):
    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1 - Adicionar / analisar")
        print("2 - Remover")
        print("3 - Alterar")
        print("4 - Ver lista")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            adicionar_produtos(conn)
        elif opcao == "2":
            remover_produtos(conn)
        elif opcao == "3":
            alterar_produto(conn)
        elif opcao == "4":
            listar_produtos(conn)
        elif opcao == "0":
            print("Programa encerrado.")
            raise SystemExit
        else:
            print("Opção inválida. Tente novamente.")
