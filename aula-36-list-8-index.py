#aula-36-list-8-index.py
"""
Métodos/Funções para lista: INDEX()

É usado para encontrar o índice da primeira ocorrência de um valor
especificado em uma lista. Se o valor não for encontrado,
o método gera um erro.

Sintaxe:
lista.index(element, start, end)

Observação: start e end são opcionais.
"""
import os
os.system('cls')
print('-'*70)
print('Funções para Lista: INDEX')
print('-'*70)

entrada = input('Digite números separados por espaço: ')
numerosStr = entrada.split() #transformar em uma lista

numeros = [] #lista vazia

for num in numerosStr:
    numeros.append(int(num))

buscarNumero = int(input('Digite o número que deseja buscar: '))

if buscarNumero in numeros:
    indice = numeros.index(buscarNumero)
    print(f'O número {buscarNumero} está no indice {indice+1}')

else:
    print(f'O número {buscarNumero} não aparece na lista')

print()
print('-'*70)
