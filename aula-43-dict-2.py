#aula-43-dict-2.py
import os

os.system('cls')

def linha(x):
    print('-'*x)

linha(50)
print('Estrutura Dicionário')
linha(50)

compras = {}
pessoas = {}
cores = {}
elementos = dict()
numeros = dict()

#Atribuindo valores
compras['id'] = 1
compras['item'] = 'Caderno'
compras['valor'] = 10.80

pessoas['id'] = '0010'
pessoas['nome'] = 'Sherlock Holmes'
pessoas['endereco'] = 'Baker Street'
pessoas['numero'] = '228'
pessoas['cidade'] = 'Londres'
pessoas['pais'] = 'Inglaterra'

cores = {
    'red' : 'Vermelho',
    'green' : 'Verde',
    'blue' : 'Azul'
}

elementos['Pb'] = 'Chumbo'
elementos['Au'] = 'Ouro'
elementos['N'] = 'Nitrogenio'

numeros = {
    1 : 100,
    2 : 200,
    3: 300
}

#Saída simples
print(f'Compras: {compras}')
print(f'Pessoas: {pessoas}')
print(f'Cor RGB: {cores}')
print(f'Tabela periódica: {elementos}')
print(f'Listagem de números: {numeros}')
print()
linha(50)

