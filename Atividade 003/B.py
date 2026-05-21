"""
B. Faça um programa que receba 2 valores, faça a divisão entre eles. 
Se a divisão não for inteira, o programa deverá arredondar o resultado 
para cima e para baixo. Faça a validação para divisão por 0.

Autor: Samuel Gurgel
Data: 20/05/2026
"""

import math
import os
os.system('cls')

n1 = float(input('Informe o primeiro valor: '))
n2 = float(input('Informe o segundo valor: '))

if n2 == 0:
    print('Erro! Não existe divisão por 0')

else:
    result = n1/n2
    print(f'Resultado da divisão: {result}')

    if result == int(result):
        print(f'O resultado da divisão é um valor inteiro')
    else:
        print(f'Arredondado para baixo: {math.floor(result)}')
        print(f'Arredondado para cima: {math.ceil(result)}')
