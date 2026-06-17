"""
F# Faça um programa que gere 10 números aleatórios.
Após gerar esses números, crie duas listas novas com ordenação
ascendente e descendente.

 Autor: Samuel Gurgel
 Data: 16/06/2026

"""
import os
from random import randint

os.system('cls')

numeros = []

for i in range(10):
    numeros.append(randint(1,100))

crescente = numeros[:]
decrescente = numeros [:]

crescente.sort() #ordem crescente
decrescente.sort(reverse=True)

print(f'Original: {numeros}')
print(f'Crescente: {crescente}')
print(f'Decrescente: {decrescente}')
print()

