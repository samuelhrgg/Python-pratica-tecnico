#aula-20-1-ex-if.py

"""
Faça um programa para pedir dois valores e mostrar qual é maior.
Em seguida, mostre a soma desses valores.

"""
print()
numero1 = int(input('Digite um número: ')) #recebendo 1º valor
numero2 = int(input('Digite outro número: ')) #recebendo 2º valor

soma = numero1 + numero2

#verificando qual é maior
if numero1 > numero2:
    print(f'O número {numero1} é maior que {numero2}')
else:
    print(f'O número {numero2} é maior que {numero1}')

print(f'A soma de {numero1} + {numero2} é: {soma}')

print()