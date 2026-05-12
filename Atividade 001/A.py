"""
A. Faça um programa que peça 3 valores , depois calcule e imprima  a 
soma e a multiplicação desses valores. 

Autor: Samuel Gurgel
Data: 12/05/2026

"""
#Recebendo os valores
print()
valor1 = int(input('Informe o 1º valor: '))
valor2 = int(input('Informe o 2º valor: '))
valor3 = int(input('Informe o 3º valor: '))

#Calculando os valores
soma = (valor1 + valor2 + valor3)
multi = (valor1 * valor2) * valor3

print()
print(f'A soma dos valores é {soma}')
print(f'A multiplicação dos valores é {multi}')
print()