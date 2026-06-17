"""
G#.Faça um programa que sorteia os números da Mega Sena e da 
Lotofácil

 Autor: Samuel Gurgel
 Data: 16/06/2026

"""
from random import randint

megaSena = []

while len(megaSena) < 6:
    numero = randint(1,60)

    if numero not in megaSena:
        megaSena.append(numero)

megaSena.sort() #colocar na ordem crescente

lista = []
acertos = 0
for x in range(6):
    numero = int((input(f'Informe o {x+1}º valor: ')))
    lista.append(numero)

    if numero in megaSena:
        acertos += 1

print(f'Números sorteados: {megaSena}')
print(f'Números jogados: {lista}')
print(f'Quantidade de acertos: {acertos}')
print()
