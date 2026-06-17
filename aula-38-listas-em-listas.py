"""
Lista dentro de listas
As listas podem conter outros objetos, inclusive outras listas.
Isso é conhecido como listas aninhadas ou listas dentro de listas.

As listas aninhadas permitem criar estruturas de dados mais complexas.

Matrizes são um exemplo comum de listas aninhadas, onde
cada elemento da lista principal é outra lista que representa
uma linha da matriz.

Exemplo:
matriz = [
        [1,2,3]
        [4,5,6]
        [7,8,9]
        ]

"""

import os
os.system('cls')

salas = [ #3 linhas de listas e 3 'colunas' de listas
        #0     1     2
    ['Maria','João','Ana'],#0
        #0      1          2
    ['Pedro', 'Tiago', 'Fábio'], #1
        #0         1        2
    ['Arthur', 'Felipe', 'Mateus'] #2
]
print('Primeira sala: ',salas[0]) #Acessando a primeira linha inteira
print('Segunda sala: ',salas[1]) #Acessando a segunda linha inteira
print('Terceira sala: ',salas[2]) #Acessando a tercceira linha inteira
print()
print('Segundo aluno, primeira sala: ', salas[0][1])
print('Terceiro aluno, segunda sala: ', salas[1][2])
print('Primeiro aluno, terceira sala: ', salas[2][0])

for sala in salas: #para cada sala na lista 'salas'
    print(sala)
    for aluno in sala:
        print(aluno)

#Criar uma matriz com for aninhado
os.system('cls')
matriz = []

for x in range(3):
    print(f'Digite os valores da linha {x+1}: ')
    linha = []
    for y in range(3):
        valor = input('Informe um valor: ')
        linha.append(valor)

    matriz.append(linha)

print(matriz)

#Imprimindo linha a linha
for x in matriz:
    for valor in x:
        print(valor, end = ' ')
    print()