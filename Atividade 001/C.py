"""
C. Faça um programa que peça 4 notas, após a 
entrada de dados calcular a média das notas digitadas.

Autor: Samuel Gurgel
Data: 12/05/2026

"""
print('-'*40)
print('Calculando média das notas')
#recebendo as notas
print()
nota1 = float(input('Informe a 1ª nota: '))
nota2 = float(input('Informe a 2ª nota: '))
nota3 = float(input('Informe a 3ª nota: '))
nota4 = float(input('Informe a 4ª nota: '))
print()

#calculando as notas
soma = (nota1 + nota2 + nota3 + nota4)
media = soma / 4

print(f'A média das notas informadas é {media}')
print()
print('-'*40)



