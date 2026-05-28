# d) Faça um programa que leia uma frase e depois exiba:
# - a frase em minúsculas
# - a frase em maiúsculas
# - a quantidade de caracteres
# - quantas letras tem a 2ª palavra

# Autor: Samuel Gurgel
# Data: 26/05/2026

frase = input('Digite uma frase: ').strip()

minuscula = frase.lower() #colocar em minusculo
maiuscula = frase.upper() #colocar em maiúsculo

palavras = frase.split() #separar a string em uma lista

segundaPalavra = palavras[1]
qtdLetras = len(palavras[1])
qtdCaract = len(frase)

print(f'Frase em minúsculas: {minuscula}')
print(f'Frase em maiúsculas: {maiuscula}')
print(f'Quantidade geral de caracteres: {qtdCaract}')
print(f'Quantidade caracteres 2ª palavra: {qtdLetras}')
