#aula-43-dict-1.py
"""
Dicionários em Python(tipo Dict)
Dicionários são estruturas de dados do tipo par de 'chave' e 'valor'

Chaves podem ser consideras como o 'indice' que vimos na lista e
podem ser de tipos imutáveis como: str, int, float, bool, tuple, etc.

O valor pode ser de qualquer tipo, incluindo outro dicionário.
Usamos a chave - {} - ou a classe dict para criar dicionários

Imutáveis: str, int, float, bool, tuple
Mutável: list, dict

"""
import os
os.system('cls')

pessoa = {}
print(pessoa, type(pessoa))

#Vamos preencher a dicionário
pessoa = {
    'Nome':'Samuel',
    'Idade':'18'
}
print(pessoa)

pessoa_2 = dict(nome = 'Samuel', sobrenome = 'Gurgel')
print(pessoa_2)

#Imprimindo elemento específico
print(pessoa_2['nome'])
print(pessoa_2['sobrenome'])

#Manipulando chaves e valores em dicionarios
chave = 'nome'
pessoa_2[chave]='Pedro'
print(pessoa_2)

