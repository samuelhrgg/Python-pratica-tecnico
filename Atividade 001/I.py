"""
I. Faça um programa que receba um valor em reais,
depois calcule quantos dólares daria para comprar
com esse valor.

"""
print('-'*70)
real = float(input("Informe um valor em reais: "))
dolar = 4.91
conversao = real/dolar

print(f'R$ {real:.2f} reais daria para comprar ${conversao:.2f} USD')
print()