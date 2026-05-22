#aula-31-funcoes-string.py
"""
Funções de Strings
As funções de string em python são métodos integrados (built-in)
que permitem realizar uma variedade de operações em objetos do tipo
string.Elas são utilizadas para manipular e transforma strings de diversas
maneiras, desde a modificação do conteúdo até a realização de buscas
e formatações.

Algumas das principais funções de string em Python:

len(): retorna o comprimento (número de caracteres) de uma string
lower(): converte todos os caracteres da string para minúsculas
upper(): converte todos os caracteres da string para maiúsculas
capitalize(): converte o primeiro caractere da string para maiúscula e os demais para minúscula
strip(): remove os espaços em branco (ou outros caracteres especificados) do início e do final da strings
replace(substring, new_string): substitui todas as ocorrências de uma substring por uma nova string.
split(sep): Divide a string em substrings com base no separador especificado e retorna uma lista das substrings resultantes.
join(iterable): Une os elementos de um iterable (ex.: lista) em uma única string, usando 


"""

import os

os.system('cls')

#Colocando largura fixa em strings ''padding''

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')  # > adicionando caracteres na esquerda
print(f'{variavel: <10}.') # < adicionando caracteres na direita
print(f'{variavel: ^11}.') # ^ ''centralizando''
print('-'*30)
print(f'{variavel:-^30}')

os.system('cls')

linha=('-'*70)
print(linha)
print('Funções String')
print(linha)

frase1 = 'Olá Mundo!'

#contar caracteres
quantidadeCaracteres = len(frase1)
print(f'A frase {frase1} possui {quantidadeCaracteres} caracteres')
print(linha)

#frase em minúsculo
minusculas = frase1.lower()
print(f'Frase original: {frase1}')
print(f'Frase em minúsculo: {minusculas}')
print(linha)

#frase em maiúsculo
maiusculas = frase1.upper()
print(f'Frase Original: {frase1}')
print(f'Frase em maiúsculo: {maiusculas}')

#frase captalizada
captalizada = frase1.capitalize()
print(f'Frase Original: {frase1}')
print(f'Frase captalizada: {captalizada}')
print(linha)

#retirar excesso espaços antes e depois
frase2 = '   Olá, mundo cruel!   '
semEspaco = frase2.strip()
print(f'Frase Original: {frase2}')
print(f'Frase sem espaços: {semEspaco}')
print(linha)

#substituição de palavras
substituicao = frase1.replace('Mundo','Python')
print(f'Frase Original: {frase1}')
print(f'Frase nova: {substituicao.replace('!','-')}')
print(linha)

#separar as palavras de um str em uma lista
lista = frase1.split(' ')
print(f'Frase original: {frase1}')
print(f'Frase separada em lista: {lista}')
print(linha)

#transforma uma lista em uma string com separador
lista2 = ['Olá','Mundo']
juncao = '-'.join(lista2)
print(f'Frase Original: {lista2}')
print(f'Frase nova: {juncao}')
print(linha)
