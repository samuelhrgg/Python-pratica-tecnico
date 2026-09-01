
from cadastro import * #importando todas funções do módulo cadastro
from calculo import *
import os, time

os.system('cls')


produtos = []
titulo = 'Sistema de Produtos'

while True:
    print('-'*70)
    print(f'{titulo:-^70}')
    print( '[1] Cadastrar produtos',
         '\n[2] Listar produtos',
         '\n[3] Buscar produtos',
         '\n[4] Calcular valor total estoque',
         '\n[5] Mostrar produto(s) mais caro(s),' \
         '\n[6] Alterar quantidade',
         '\n[0] Sair'  )
    
    opcao = input('Escolha uma opção:')
    print()

    if opcao == '1':
        nome = input('Nome do produto: ').strip() #Remover os espaços extras

        if not nome:
            print('O nome não pode ficar vazio.')
            continue
        try:
            preco = float(input('Preço: '))
            quantidade = int(input('Quantidade em estoque: '))

            if preco <= 0:
                print('O preço deve ser maior que zero')
                continue #voltar pro while

            if quantidade < 0:
                print('A quantidade não pode ser negativa')
                continue

        except ValueError:
            print('Digite valores númericos válidos')
            continue

        cadastrado = cadastrar_produto(produtos, nome, preco, quantidade)

        if cadastrado:
            print('Produto cadastro com sucesso!')
        else:
            print('Já existe um produto com esse nome.')

    elif opcao == '2':
        listar_produtos(produtos)

    elif opcao == '3':
        nome = input('Digite o nome do produto: ').strip()

        produto = buscar_produto(produtos, nome)

        if produto:
            print('Produto encontrado:')
            print(f'Nome: {produto['nome']}')
            print(f'Preço: {produto['preco']:.2f}')
            print(f'Quantidade: {produto['quantidade']}')

        else:
            print('Produto não encontrado')

    elif opcao == '4':
        total = calcular_total_estoque(produtos)
        print(f'Valor total do estoque: R$ {total:.2f}')

    elif opcao == '5':
        produtosMaisCaros = produtos_mais_caros(produtos)

        if not produtosMaisCaros:
            print('Nenhum produto cadastrado!')
        else:
            print('----------- Produto(s) mais caro(s) -----------')

            for produto in produtosMaisCaros:
                print(
                    f'{produto['nome']}',
                    f'R$ {produto['preco']:.2f}'
                )

    elif opcao == '6':

        
        nome = input('Digite o nome do produto: ')
        produto = buscar_produto(produtos,nome)

        if produto is None:
            print('Produto não encontrado')
            continue

        else:
            try:
                nova_quantidade = int(input('Digite a nova quantidade: '))

                if nova_quantidade < 0:
                    print('A quantidade não pode ser negativa')
                    continue

            except ValueError:
                print('Digite uma quantidade válida.')
                continue

            alterar_quantidade(produtos,nome,nova_quantidade)

            print('Produto cadastrado com sucesso!')

    elif opcao == '0':
        print('Encerrando o programa...')
        time.sleep(3)
        print('Programa encerrado!')
        break

    else:
        print('Opção inválida!')
