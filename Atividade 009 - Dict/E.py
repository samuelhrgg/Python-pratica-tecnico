"""
E. Faça um programa para criar um dicionário com 5  
ferramentas. Depois,  imprima os valores e a quantidade de
elementos do dicionário.


Autor: Samuel Gurgel
Data: 15/07/26
"""

ferramentas = {
    'Martelo' : '5 unidades',
    'Alicate' : '10 unidade',
    'Chave philips' : '20 unidades',
    'Chave de Fenda' : '8 unidades',
    'Serrote' : '12 unidade'
}

print('Valores das ferramentas:')

for ferramenta in ferramentas.values():
    print(ferramenta)

print(f'\nQuantidade: {len(ferramentas)}')
