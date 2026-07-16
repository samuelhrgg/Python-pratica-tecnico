"""
I. .Faça um programa para criar um dicionário com 4 elementos.
Depois imprima a lista completa, delete o último elemento e
mostre uma listagem nova.

Autor: Samuel Gurgel
Data: 15/07/26
"""

dados = {
    'nome' : 'Ana',
    'idade' : 18,
    'cidade' : 'Belo Horizonte',
    'curso' : 'informatica'
}

print('Original')
print(dados)

dados.popitem() #sempre a última chave

print('-'*50)
print('Dicionário atualizado:')
print(dados)

