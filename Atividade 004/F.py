# f) Faça um programa que receba o nome completo de uma pessoa
# e imprima esse nome separadamente.
# Autor: Samuel Gurgel
# Data: 26/05/2026

nomeCompleto = input('Digite o nome completo: ').strip().title()

partes = nomeCompleto.split() #divide em partes

print(f'Nomes separados: {partes}')