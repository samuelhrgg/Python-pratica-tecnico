"""
A#. Faça um programa que receba um valor e mostre sua raiz quadrada. 
Para raízes que não são exatas, arredonde para cima ou para baixo. 
Faça a validação para números negativos, avisando ao usuário que o 
resultado será um número complexo.

Autor: Samuel Gurgel
Data: 20/05/2026
"""
import math
import os

os.system('cls')
numero = float(input('Digite um número: '))

#se o número for menor que 0
if numero < 0:
    print(f'Atenção, a raiz quadrado de {numero} será um valor complexo!')
 
else:
    raiz = math.sqrt(numero)

    if raiz == int(raiz):
        print(f'A raiz exata de {numero} é {raiz}')
    else:
        print(f'A raiz de {numero} não é exata!')

        print(f'Arredondadamento para baixo: {math.floor(raiz)}')

        print(f'Arredondadamento para cima: {math.ceil(raiz)}')
