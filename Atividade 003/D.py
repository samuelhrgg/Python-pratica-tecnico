"""
D. Faça um programa para sortear um número de 1 a 20.

Autor: Samuel Gurgel
Data: 20/05/2026

"""
import random
import os

os.system('cls')

inciar = input('Pressione [enter] para sortear um número de 1 à 20: ')

numero = random.randint(1,20)

print(f'O número sorteado foi {numero}')