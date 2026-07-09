#aula-43-dict-5-items,keys,value.py
"""
items() → Retorna uma visão dos pares(chave, valor) do dicionário

keys() → Retorna uma visão das chaves do dicionário

values() → Retorna uma visão dos valores do dicionário

"""
import os
os.system('cls')

meuDicionario = {}

while True:
    print('Menu de Opções')
    print('1 - Adicionar um par chave-valor')
    print('2 - Mostrar chaves do dicionário')
    print('3 - Mostrar valores do dicionário')
    print('4 - Mostrar itens do dicionário')
    print('5 - Sair')

    opcao = input('Escolha uma opção (1-5): ')
    if opcao == '1':
        #Adicionar uma par chave-valor ao dicionário:
        chave = input('Digite a chave: ')
        valor = input('Digite um valor: ')
        meuDicionario[chave] = valor
        print(f'Par {chave} : {valor} adicionado!')
    
    elif opcao == '2':
        #Mostrar as chaves do dicionário usando keys()
        if meuDicionario: #Se não estiver vazio, ou seja, não for falso
            print(f'A chave do dicionário: {meuDicionario.keys()}')
        else:
            print('O dicionário está vazio. Adicione itens primeiro')
    elif opcao == '3':
        #Mostrar os valores do dicionário usando values()
        if meuDicionario:
            print(f'Valores do dicionario: {meuDicionario.values()}')
        else:
            print('O dicionário está vazio. Adicione itens primeiro')
    
    elif opcao == '4':
        #Mostrar os itens (chave-valor) do dicionaro usando items()
        if meuDicionario:
            print(f'Itens do dicionário: {meuDicionario.items()}')
        else:
            print('O dicionário está vazio. Adicione itens primeiro')    
    
    elif opcao == '5':
        #sair do programa
        print('Saindo do programa...')
        break

    else:
        print('Opção inválida')
    

#Outro exemplo utilizando FOR
#items() retorna pares(chave, valor)
#Dicionário
aluno = {
    'Nome':'Samuel',
    'Idade' : 27,
    'Curso' : 'Python'
}
print('-'*70)

for x in aluno.items():
    print(x)
print('-'*70)

print(aluno)

print('-'*70)

for x in aluno.keys():
    print(x)