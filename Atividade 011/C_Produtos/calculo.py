#CÁLCULOS DO SISTEMA:

#CALCULAR TOTAL ESTOQUE
def calcular_total_estoque(produtos):

    total = 0
    for produto in produtos:
        total += produto['preco'] * produto['quantidade']

    return total

#CALCULO PRODUTO(S) MAIS CARO(S):
def produtos_mais_caros(produtos):

    maior_preco = 0
    for produto in produtos:
        if produto['preco'] > maior_preco:
            maior_preco = produto['preco']

    produtosMaisCaros = []

    for produto in produtos:
        if produto['preco'] == maior_preco:
            produtosMaisCaros.append(produto)

    return produtosMaisCaros