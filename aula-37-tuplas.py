#aula-37-tuplas.py
"""
Tuplas em Python

Tuplas são estruturas de dados imutáveis, ou seja, uma vez criadas,
seus elementos não podem ser alterados.

São úteis quando você desejar armazenar um conjunto de valores que 
não devem ser modificados, como coordenadas, dados de configuração,
ou qualquer outra informação que deve permanecer constante. 


"""
import os

os.system('cls')

#Criando uma tupla
coordenadas = (10.0, 20.0)
print(coordenadas)

#Acessar elementos da tupla:
print(coordenadas[0]) #primeiro elemento
print(coordenadas[1]) #segundo elemento

#Tuplas são imutáveis, então não podemos alterar os elementos:
#coordenadas[0] = 5.0 #gerar um erro.

nomes = ['Maria','João','Ana'] #lista
#Criando uma tupla a partir de uma lista
tuplaNomes = tuple(nomes) #tupla
print(tuplaNomes)
listaTupla = list(tuplaNomes)
print(listaTupla)

#Acessando uma lista dentro da tupla
tuplaTeste = (1,2,3,['Frank','Fabio'])
tuplaTeste[3][0] = 'Samuel'
print(tuplaTeste)

#Criando outra tupla:
tuplaCores = ('vermelho','verde','azul')
print(tuplaCores.index('verde'))
print(tuplaCores.count('azul'))
