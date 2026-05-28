# e) Faça um programa que receba uma frase e mostre
# quantas vezes as vogais foram utilizadas.
# Autor: Samuel Gurgel
# Data: 26/05/2026

frase = input('Digite uma frase:').lower()

a = frase.count('a') + frase.count('à') + frase.count('â') + frase.count('á') + frase.count('ã')
e = frase.count('e') + frase.count('é') + frase.count('ê') 
i = frase.count('i') + frase.count('í') 
o = frase.count('o') + frase.count('ó') + frase.count('ô') + frase.count('õ') 
u = frase.count('u') + frase.count('ú') 

soma = a+e+i+o+u
print(f'Quantidade de "a": {a}')
print(f'Quantidade de "e": {e}')
print(f'Quantidade de "i": {i}')
print(f'Quantidade de "o": {o}')
print(f'Quantidade de "u": {u}')
print(f'Total de vogais: {soma}')
