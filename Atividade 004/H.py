# i) Faça um programa que receba o nome completo de uma pessoa
# e mostre o primeiro e o último nome.
# Autor: Samuel Gurgel
# Data: 26/05/2026

nomeCompleto = input('Informe seu nome completo: ').strip()

partes = nomeCompleto.split()

primeiroNome = partes[0]
ultimo = partes[-1]

print(f'Primeiro nome: {primeiroNome}')
print(f'Último nome: {ultimo}')
