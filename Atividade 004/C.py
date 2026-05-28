# c) Faça um programa que leia o nome de uma pessoa e verifique
# se a palavra "Oliveira" está presente neste nome.

# Autor: Samuel Gurgel
# Data: 26/05/2026

nome = input('Digite um nome: ').strip()

resultado = 'oliveira' in nome.lower()

if resultado:
    print(f'Oliveira está presente no nome {nome}')

else:
    print(f'Oliveira não está presente no nome {nome}')