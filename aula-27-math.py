#aula-27-math.py
"""
Biblioteca math

A biblioteca math em Python fornece um conjunto abrangente de funções 
matemáticas para realizar operações matemáticas avançadas. 
Essas funções são úteis quando você precisa lidar com cálculos 
mais complexos que não são suportados pelos operadores matemáticos padrão.

Funções mais comuns da biblioteca math:

math.ceil(x) → Retorna o arredondamento para cima.
math.floor(x) → Retorna o arredondamento para baixo.
math.pow(x, y) → Retorna x elevado à potência y..
math.sqrt(x) → Retorna a raiz quadrada de x.

"""

import os
import math

#Limpando terminal
os.system('cls')
print('-'*70)
print('Estudo da Biblioteca Math')
print('-'*70)
print()

#entrada de dados
numeroDecimal = float(input('Informe um valor decimal: '))

#arredondar para cima
praCima = math.ceil(numeroDecimal)
print(f'O número {numeroDecimal} arredondado para cima é: {praCima}')

#arredondar para baixo
praBaixo = math.floor(numeroDecimal)
print(f'O número {numeroDecimal} arredondado para baixo é: {praBaixo}')
print()
print('-'*70)

#Potência
x = int(input('Informe um valor: '))
y = int(input(f'Gostaria de elevar {x} à qual potência: '))
potencia = math.pow(x,y)
print(f'{x} elevado à {y} é: {potencia}')

#Raiz
print('-'*70)
raiz = int(input('Informe um valor para descobri a raiz: '))
raizQuad = math.sqrt(raiz)
print(f'A raiz quadrada de {raiz} é {raizQuad}')
print()