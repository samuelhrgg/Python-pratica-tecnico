#aula-36-list-10-reverse.py
"""
Métodos/Funções para listas: reverse()

É usado para inverter a ordem dos elementos em uma lista.
Diferente de sort(), reverse não ordena os elementos,
apenas inverte a ordem atual.

Sintaxe:
lista.reverse()
"""
import os
os.system('cls')

print('-'*70)
print('Funções para lista: Reverse')
print('='*70)

entrada = input('Digite números separados por espaço: ')
numerosStr = entrada.split()
numeros = []

#convertendo a lista de strings em uma lista de inteiro
for num in numerosStr:
    numeros.append(int(num))

print()
print(f'Lista fornecida incialmente: {numeros}')

#lista invertida
numeros.reverse()
print(f'Lista invertida: {numeros}')
print()
print('='*70)
