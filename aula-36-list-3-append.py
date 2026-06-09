#aula-36-list-3-append.py

"""
Métodos/funções para Listas: append()

É utilizada para adicionar um elemento ao final de uma lista existente.
É uma função embutida em python e não retorna um novo objeto,
mas modifica a lista original.

Sintaxe:
lista.append(elemento)
"""
import os
os.system('cls')

linha = ('-'*70)
print(linha)
print('Funções para lista: APPEND')
print(linha)

listaNumeros = [] #Lista vazia

for i in range(3):
    numero = int(input('Digite um número: '))

    #adicionar um valor na lista
    listaNumeros.append(numero)
    
#exibindo a lista
print(listaNumeros)
#adicionando mais um elemento
listaNumeros.append('Samuel')
#exibindo a lista novamente com o último elemento adicionado
print(listaNumeros)