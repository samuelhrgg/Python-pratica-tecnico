#Sistema cadastro de Livros

import os
os.system('cls')

livros = []

while True:
    print('='*40)
    print('Sistema de Cadastro')
    print('='*40)
    print('[1] Cadastrar livro')
    print('[2] Listar livros')
    print('[3] Alterar livro')
    print('[4] Excluir livro')
    print('[5] Sair')
    print('='*40)

    opcao = input('Escolha uma opção: ')

    #CADASTRAR LIVROS
    if opcao == '1':
        titulo = input('Título: ').strip()
        autor = input('Autor: ').strip()

        if titulo == '' or autor == '':
            print('\nDados inválidos!')
        else:
            livros.append([titulo,autor])
            print('\nLivro cadastrado com sucesso!')
    
    #LISTAR LIVROS
    elif opcao == '2':
        if len(livros) == 0:
            print('\nNenhum livro cadastrado!')
        else:
            print('\nLista de Livros:')
            for i in range(len(livros)):
                print(f'{i+1}. {livros[i][0]} - {livros[i][1]}')

    #ALTERAR LIVROS
    elif opcao == '3':
        if len(livros) == 0:
            print('\nNenhum livro cadastrado!')

        else:
            print('Livros Cadastrados')
            for i in range(len(livros)):
                print(f'{i+1}. {livros[i][0]}')
            
            try:
                indice = int(input('Qual livro deseja alterar: '))-1

                if indice >= 0 and indice < len(livros):
                    novoTitulo = input('Novo título: ').strip()
                    novoAutor = input('Novo autor: ').strip()

                    livros[indice][0] = novoTitulo
                    livros[indice][1] = novoAutor

                    print('Livro alterado com sucesso!')
                
                else:
                    print('Livro inexistente!')
            except:
                print('Digite apenas números!')

    #EXCLUIR LIVRO
    elif opcao == '4':

        if len(livros)==0:
            print('Nenhum livro cadastrado!')
        
        else:
            print('Livros cadastrados:')

            for i in range(len(livros)):
                print(f'{i+1}. {livros[i][0]}') 
            
        try:
            indice = int(input('Qual livro deseja excluir: '))-1

            if indice >= 0 and indice < len(livros):

                del livros[indice]
                
                print('Livro excluido com sucesso!')

            else:
                print('Livro inexistente!')

        except:
            print('Digite apenas números!')
        
    #SAIR
    elif opcao == '5':
        print('Programa encerrado!')
        break

    #OPÇÃO INVÁLIDA
    else:
        print('Opção inválida, digite de 1 à 5!')

        
