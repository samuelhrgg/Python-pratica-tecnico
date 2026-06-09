"""
Fatiando uma lista
Para executar o fatiamento de uma lista, basta seguir os mesmos
passos de fatiamento de uma String em Python

Utilizamos colchetes após a variável e sem seguida declaramos:
inicio, fim, intervalo (passo)

"""
import os
os.system('cls')
linha = ('-'*50)

print(linha)
print('ESTRUTURA DE DADOS: LISTAS [ ]')
print(linha)

listaMista = ['a', 'b', 3 , 'c' , 100]

listaFatiada1 = listaMista[0:] #busca todos elementos
listaFatiada2 = listaMista[0:3] #busca até o indice 3
listaFatiada3 = listaMista[::2] #todos elementos de 2 em 2
listaFatiada4 = listaMista[::-1] #todos elementos de trás pra frente

print()
print(f'Fatiando primeiro indice da lista: {listaMista[0]}')
print(f'Buscando todos elementos da lista: {listaFatiada1}')
print(f'Buscando até o indice 3 da lista: {listaFatiada2}')
print(f'Buscando todos elementos de 2 em 2: {listaFatiada3}')
print(f'Buscando todos elementos de trás pra frente: {listaFatiada4}')
print()
print(linha)