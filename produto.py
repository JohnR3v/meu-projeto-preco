from database import buscar_produto, salvar_produto


def ler_preco(mensagem):
    while True:
        valor = input(mensagem).strip().replace(",", ".")
        try:
            return float(valor)
        except ValueError:
            print("Valor inválido. Digite um número válido, por exemplo: 10.50")


def calcular_variacao_percentual(preco_anterior, preco_atual):
    if preco_anterior == 0:
        return 0.0
    return ((preco_atual - preco_anterior) / preco_anterior) * 100


def classificar_situacao(variacao_percentual):
    if variacao_percentual > 0:
        return "Aumento"
    elif variacao_percentual < 0:
        return "Redução"
    else:
        return "Mantido"


def processar_produto(conn, nome, mercado):
    registro = buscar_produto(conn, nome, mercado)

    if registro:
        _, preco_atual_anterior, _ = registro
        preco_anterior = preco_atual_anterior
        print(f"Produto já cadastrado em {mercado}. Usando o último preço atual: R$ {preco_anterior:.2f}")
    else:
        preco_anterior = ler_preco("Preço do mês anterior: ")
        print(f"Primeiro cadastro em {mercado}.")

    preco_atual = ler_preco("Preço do mês atual: ")
    diferenca = preco_atual - preco_anterior
    variacao_percentual = calcular_variacao_percentual(preco_anterior, preco_atual)
    situacao = classificar_situacao(variacao_percentual)

    salvar_produto(conn, nome, mercado, preco_anterior, preco_atual)

    print(f"Produto: {nome}")
    print(f"Mercado: {mercado}")
    print(f"Diferença: R$ {diferenca:.2f}")
    print(f"Variação: {variacao_percentual:.2f}%")
    print(f"Situação: {situacao}")
