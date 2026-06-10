#aula-36-list-9-sort.py
"""
Métodos/Funções para Listas: sort()

É usado para ordenar os elementos de uma lista em ordem ascendente
por padrão. Ele também pode ordenar os elementos em ordem descendente 
ou personalizada usando parâmetros opcionais.

Sintaxe:
lista.sort(key=None, reverse=False)
"""
import os
os.system('cls')
print('-'*70)
print('Funções para lista: SORT')
print('-'*70)

entrada = input('Digite números separados por espaço: ')
numerosStr = entrada.split() #transformar em uma lista

numeros = [] #lista vazia

for num in numerosStr:
    numeros.append(int(num))

ordem = input('Digite "cres" para ordem "crescente" ou ' \
              '"decr" para ordem decrescente:').strip().lower()

print()
print(f'Lista fornecida inicialmente: {numeros}')
print()
if ordem == 'cres':
    numeros.sort()
    print(f'Lista ordenada em ordem crescente: {numeros}')

elif ordem == 'decr':
    numeros.sort(reverse=True)
    print(f'Lista orndenada em ordem decrescente: {numeros}')

else:
    print('Opção inválida, a lista não foi ordenada.')

print()
print('-'*70)

names = ['Gilberto','Karlos','Luan','Vardiero','Kvaratskhelia','Aislan']
print(f'Lista original: {names}')

names.sort()
print(f'Lista em ordem alfabética A-Z: {names}')

names.sort(reverse=True)
print(f'Lista em ordem alfabética Z-A: {names}')

names.sort(key=len)
print(f'Nomes do menor para o maior: {names}')

names.sort(reverse=True,key=len)
print(f'Nomes do maior para o menor: {names}')

print()
print('-'*70)
