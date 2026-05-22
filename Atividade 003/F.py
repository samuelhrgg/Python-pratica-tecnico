"""
F#. Faça um programa que peça os valores de a, b e c 
de uma equação do 2º grau. Calcule as raízes da equação do
2º grau seguindo a fórmula: Δ = b² - 4ac, x = (-b ± raiz(Δ)) / (2a).

Autor: Samuel Gurgel
Data: 20/05/2026

Δ > 0 → duas raízes reais diferentes
Δ = 0 → uma raiz real
Δ < 0 → não existem raízes reais (raízes complexas)

"""
import math
print('=== Equação do 2º Grau ===')

a = float(input('Digite o valor de a: '))
b = float(input('Digite o valor de b: '))
c = float(input('Digite o valor de c: '))

#validação para verificar se é equação de 2º grau:
if a == 0:
    print('Não é equação do 2º grau, pois a = 0')
else:
    #cálculo do delta
    delta = b**2 - 4*a*c #b² - 4 * a * c
    print(f'Delta = {delta}')

    #caso delta seja maior que 0:
    if delta > 0:
        #cálculo da primeira raiz
        x1 = (-b + math.sqrt(delta)) / (2*a)
        
        #cálculo da segunda raiz
        x2 = (-b - math.sqrt(delta)) / (2*a)
    
        print('A equação possui duas raizes reais diferentes.')
        print(f'XI = {x1}')
        print(f'XII = {x2}')

    #caso em que delta é igual a 0
    elif delta == 0:
        #calculo da única raiz real
        x = (-b)/(2*a)

        print('A equação possui apenas uma raiz real')
        print(f'X = {x}')
    #caso em que delta é menor que 0
    else:
        print('A equação não possui raizes reais')
        print('O resultado possui raízes complexas.')



