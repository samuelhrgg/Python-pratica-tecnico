#aula-36-list-6-pop.py
"""
Métodos/funções para listas: pop()

É uma função usada em listas que remove e retorna o elemento
no índice especificado. Se nenhum índice for fornecido, pop()
remove e retorna o último elemento da lista.

Se a lista estiver vazia e pop() for acionado, isso resulturá
em um ERRO.

Sintaxe:
lista.pop(indice)

"""

import os
os.system('cls')

print('-'*70)
print('Funções em para lista: POP')
print('-'*70)

lista = [10,20,30,40,50,60,70,80,90,100]
print(f'Lista atual: {lista}')
item = int(input('Digite o índice do item a ser removido'\
                f'de 0 à {len(lista)}: '))
print()

if item >= 0 and item <= len(lista):
    elementoRemovido = lista.pop(item)
    print(f'Elemento Removido: {elementoRemovido}')

else:
    print(f'Posição fora do intervalo 0,{len(lista)}')

print()
print(f'Lista após remoção: {lista}')
print(f'Tamanho da nova lista: {len(lista)}')
print()
