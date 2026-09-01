# Funções de Cadastro

#FUNÇÃO CADASTRAR PRODUTO:
def cadastrar_produto(produtos, nome, preco, quantidade):

    for produto in produtos:
        if produto['nome'].lower() == nome.strip().lower():
            return False

    produtos.append({
        'nome' : nome.strip(),
        'preco' : preco,
        'quantidade': quantidade
    })

    return True

#FUNÇÃO LISTAR PRODUTOS:
def listar_produtos(produtos):
    if not produtos:
        print('Nenhum produto cadastrado!')
        return #parar a execução dessa função 

    print('----------- Produtos Cadastrados -----------')
    for produto in produtos:
        print(f'Nome: {produto['nome']}')
        print(f'Preço: {produto['preco']:.2f}') #formatar com 2 caracteres
        print(f'Quantidade: {produto['quantidade']}')
        print()


#FUNÇÃO BUSCAR PRODUTO:
def buscar_produto(produtos,nome):

    for produto in produtos:
        if produto['nome'].lower() == nome.strip().lower():
            return produto

    return None

#FUNÇÃO ALTERAR QUANTIDADE:
def alterar_quantidade(produtos, nome, nova_quantidade):
    produto = buscar_produto(produtos, nome)

    if produto is None:
        return False

    else:
        produto['quantidade'] = nova_quantidade
        return True
