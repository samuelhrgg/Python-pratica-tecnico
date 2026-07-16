"""
D. Faça um programa para criar um dicionário com 5  cores.
Depois,  imprima as chaves e os valores deste dicionário.

Autor: Samuel Gurgel
Data: 15/07/26
"""

cores = {
    'Azul' : "#0099ff",
    'Verde' : "#19ff24",
    'Vermelho' : "#ff0000",
    'Amarelo' : "#EEFF00",
    'Preto' : '#252525'
}

print('Chaves:')
for chave in cores.keys():
    print(chave)

print()

print('Valores:')
for valor in cores.values():
    print(valor)

