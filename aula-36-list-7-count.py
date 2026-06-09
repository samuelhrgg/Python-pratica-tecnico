#aula-36-list-7-count.py
"""
Métodos/funções para listas: count()

É usado para contar o número de vezes que um valor específico 
aparece em uma lista. É útil quando você precisa saber a
frequência de um determinado elemento na lista.

Sintaxe:
lista.count(elemento)
"""
import os
os.system('cls')

print('-'*70)
print('Funções para lista: COUNT')

entrada = input('Digite os números separados por espaço: ')

numerosStr = entrada.split()

numeros = []

for num in numerosStr:
    numeros.append(int(num))

numerosContar = int(input('Digite o número que deseja contar: '))
contagem = numeros.count(numerosContar)

print(f'O número {numerosContar} aparece {contagem} vez(es) na lista')
print()
