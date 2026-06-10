#aula-36-list-12-clear.py
"""
Métodos/Funções para listas: Clear()

É usado para remover todos os elementos da lista, deixando-a vazia.
Ele modifica alista original e não retorna uma nova lista.

Sintaxe
lista.clear()

"""
import os
os.system('cls')

print('-'*70)
print('Funções para lista: CLEAR')
print('-'*70)

entrada = input('Digite números separados por espaço: ')

numerosStr = entrada.split()

numeros = []
for num in numerosStr:
    numeros.append(int(num))

print()
print(f'Lista fornecida incialmente: {numeros}')

#limpar lista
numeros.clear()
print(f'Lista limpa: {numeros}')
print()
