#aula-43-dict-3-clear,copy,len.py

#Métodos úteis para Dict
#Clear(), Copy() e Len()

import os
os.system('cls')

def linha(x):
    print('-'*x)

meu_Dicionario = {}

while True:
    linha(50)
    print('Menu de Opções')
    print('1 - Adicioanr um par chave-valor')
    print('2 - Mostrar dicionário')
    print('3 - Mostrar o tamanho do dicionário')
    print('4 - Fazer uma cópia do dicionário')
    print('5 - Limpar o dicionário')
    print('6 - Sair')
    linha(50)
    
    opcao = input('Escolha uma opção (1-6): ')

    if opcao == '1':
        chave = input('Digite a chave: ')
        valor = input('Digite o valor: ')
        meu_Dicionario[chave] = valor
        print(f'Par {chave} : {valor} adicionado')
    
    elif opcao == '2':
        print(f'Dicionário atual: ', meu_Dicionario)
    
    elif opcao == '3':
        #verificar o tamanho da lista
        tamanho = len(meu_Dicionario)
        print(f'O dicionário tem {tamanho} elementos')

    elif opcao == '4':
        #Criar uma cópia do dicoonário usando copy()
        copia_dicionario = meu_Dicionario.copy()
        print(f'Cópia do dicionário: {copia_dicionario}')

    elif opcao == '5':
        #Limpar o dicionário utilizando o clear()
        meu_Dicionario.clear()
    
    elif opcao == '6':
        print('Saindo do programa...')
        break

    else:
        print('Opção inválida!')
