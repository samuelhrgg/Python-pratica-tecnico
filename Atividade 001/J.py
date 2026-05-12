"""
J#. Faça um programa com entrada de dados para calcular
o perímetro de um retângulo.

Autor: Samuel Gurgel
Data: 12/05/2026

P = 2 x (comprimento + largura)

"""
print('-'*20)
print('Calculando Períemtro de Retângulo')
print()
comprimento = float(input('Digite o comprimento do retângulo (cm): '))
largura = float(input('Digite a largura do retângulo (cm): '))

#calculando perimetro
perimetro = 2 * (comprimento + largura)
print()
print(f'O perímetro desse retângulo é: {perimetro:.4f}cm')
print('-'*40)
print()
