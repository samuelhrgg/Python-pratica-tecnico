#aula-36-list-1.py
"""
Listas em Python
Em python, uma lista é estrutura de dados que pode conter uma coleção
ordenados de elementos.

Esses elementos podem ser de qualquer tipo de dado como:
números, strings, outros listas e até mesmo objetos mais complexos.

Tipo List - Mutável
Suporta vários valores de qualquer tipo

Métodos úteis: append, insert, pop, del, clear, extend, outros
"""
import os
os.system('cls')
#Strings 'comum'
linha = ('-'*50)
print(linha)
print('Acessando indices da String comum')

string = 'ABCDE' #5 caracteres (5 indices)
print(f'String: {string}')
print(f'Indice 2 da string: {string[2]}')
print()

print('Criando a lista 1ª sem elementos: ')
lista = [] #lista vazia
print(f'Lista: {lista , type(lista)}')
print(f'Lista: {lista} : {bool(lista)}') #falso pois está vazia (0)

#Exemplo 2
print(linha)
print('Criando a 2º lista com diferentes tipos')
print()
lista2 = [123, True, 'Samuel' , 1.2] #posso ter vários formatos
print(f'Lista com diferentes formatos: {lista2}')
print()

#Exemplos 3
print(linha)
print('Criando a 3ª lista com nomes')
#indices     0           1          2
lista3 = ['Aluno 1', 'Aluno 2', 'Aluno 3']
print(f'Lista inteira: {lista3}')
print(f'Indice 1 da lista: {lista3[1]}')
print(f'Função no indice da lista: {lista3[1].upper()}')
print()

print('Alterando indices da lista (manual):')
lista4 = ['Samuel','João','Gabriel']
print(f'Lista original {lista4}')
lista4[1] = 'Tiago'
print(f'Lista alterada {lista4}')
print()
print(linha)