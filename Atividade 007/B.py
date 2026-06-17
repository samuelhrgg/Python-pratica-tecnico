"""
B#.Faça um programa que preencha uma lista com 50 números 
aleatórios. Depois fatie essa lista em 5 listas de 10 elementos.
 
 Autor: Samuel Gurgel
 Data: 16/06/2026


"""
from random import randint

numeros = []

for i in range(50):
    numeros.append(randint(1,100))
    
lista1 = numeros[0:10] #não pega o 10 
lista2 = numeros[10:20] #não pega o 20 
lista3 = numeros[20:30] #não pega o 30 
lista4 = numeros[30:40] #não pega o 40 
lista5 = numeros[40:] #40 até o final

print('Listas fatiadas:')
print(f'Lista 01: {lista1}')
print(f'Lista 02: {lista2}')
print(f'Lista 03: {lista3}')
print(f'Lista 04: {lista4}')
print(f'Lista 05: {lista5}')

