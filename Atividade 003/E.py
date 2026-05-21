"""
E#. Faça um programa onde o usuário tenta adivinhar o número 
que o computador está ‘pensando’.

Autor: Samuel Gurgel
Data: 20/05/2026
"""

import random
import os

numeroSecreto = random.randint(1,20)

palpite = int(input('Tente adivinhar um número de 1 a 20: '))

if palpite == numeroSecreto:
    print('Você acertou!')

else:
    print(f'Poxa, você errou! O número era {numeroSecreto}')
