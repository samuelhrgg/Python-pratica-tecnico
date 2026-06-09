"""
Métodos/Funções para lista: insert()

sintaxe:
lista.insert(posição,elemento)

"""

import os
os.system('cls')

print('-'*70)
print('Funções para listas: INSERT')
print('-'*70)

lista = [1,2,3,4,5,6]

posicao = int(input('Posição onde desejar inserior o elemento:'))

elemento = input('Elemento à ser inserido: ')

if posicao >= 0:
    print(f'Tamanho da lista antes da inserção: {len(lista)}')
    lista.insert(posicao,elemento)
    print(f'Lista após inserção: {lista}')
    print(f'Tamanho da lista após inserção: {len(lista)}')

else:
    print(f'A posição está fora do intervalo válido!')

print()
print('-'*70)

#exemplo 2
print()
print('-'*70)
listaNova = ['Tiago','Maria','Luiz','Michele']
print(f'Lista original: {listaNova}')

listaNova.insert(10,'Samuel')
print(f'Lista modificada: {listaNova}')
print()
