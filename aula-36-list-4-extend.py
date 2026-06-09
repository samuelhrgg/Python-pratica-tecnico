#aula-36-list-4-extend.py

"""
Métodos/funções para Listas: extend()

É usado para estender uma lista adicionando os elementos de outra lista
ao final da lsita 'original'. Em outra palavras, ela anexa todos elmenetos do 
iterável fornecido ao final da lista em que a função é chamada.


Sintaxe:
lista.extend(Iteravel)
"""

import os
os.system('cls')

print('-'*70)
print('Funções para lista: EXTEND')
print('-'*70)

#Juntar duas listas manualmente
listaA = [1,2,3]
listaB = [4,5,6]
listaC = listaA + listaB
print(f'Lista A: {listaA}')
print(f'Lista B: {listaB}')
print(f'Nova lista: {listaC}')

#Utilizando o extend
listaA.extend(listaB)
print(f'Nova lista A: {listaA}')
print(f'Lista b: {listaB}')
print()
print('-'*70)

#Extend com for
listaNumeros = []
entrada = input('Digite números separados por espaço: ')

#transformar variável em uma nova lista
numeros = entrada.split() 

#criando lista para armazenar números pares
pares = []

for x in numeros: #para cada elemento da minha lista numeros
    numeroAuxiliar = int(x)

    if numeroAuxiliar % 2 == 0:
        pares.append(numeroAuxiliar)

#Usando extend para adicionar todos números pares à lista principal
listaNumeros.extend(pares)

print(f'Número pares adicionados: {listaNumeros}')