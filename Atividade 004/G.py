# h) Faça um programa que leia o nome de um aluno e mostre:
# - quantas vezes a letra "o" aparece
# - a posição da primeira vez
# - a posição da última vez

# Autor: Samuel Gurgel
# Data: 26/05/2026

nome = input('Digite o nome do aluno: ').lower().strip()

quantidade = nome.count('o')
primeira = nome.find('o') #qual posição que aparece a letra 'o' na primeira vez
ultima = nome.rfind('o') #qual posição ele parece de trás pra frente

if 'o' not in nome:
    print(f'Não existe a letra "o" no nome {nome}')
    
else:
    print(f'Quantidade de letras "o": {quantidade}')
    print(f'Primeira posição: {primeira+1}')
    print(f'última posição: {ultima+1}')
