#aula-list-14-enumerate.py
"""
Imprimindo valores da lista com Enumerate

enumerate - enumera iteráveis (indices)
"""
import os
os.system('cls')
print('-'*70)
print('Utilizando do enumerate')
print('-'*70)

lista = ['Sofia','Mariana','Rafaela']

for item in enumerate(lista):
#cria uma lista para item da lista
    print(item)
print()

for x in enumerate(lista):
    a,b = x
    print(a,b)
print()

for a,b in enumerate(lista):
    print(a,b)

for indice,nome in enumerate(lista):
    print(f'Indice: {indice} | Nome: {nome}')

print()

