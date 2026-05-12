"""
D#. Faça um programa que receba e divida 2 números. 
A saída da divisão precisará ser formatada com 4 casas decimais.

Autor: Samuel
Data: 12/05/2026

"""

print()
print('Divisão de 2 valores')
numero1 = float(input('Informe o primeiro valor: '))
numero2 = float(input('Informe o segundo valor: '))

#calculando
divisao = (numero1 / numero2)
print(f'A divisão do número {numero1} por {numero2} é {divisao:.4f}')
print()