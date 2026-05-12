"""
 Faça um programa que peça o ano do 
 seu nascimento e calcule quantos anos você faz esse ano.

 Autor: Samuel Gurgel
 Data: 12/05/2026

"""
print()
anoAtual = int(input('Informe o ano atual (AAAA): '))
nascimento = int(input('Informe seu ano de nascimento (AAAA): '))
idade = anoAtual - nascimento
print()
print(f'Sua idade é: {idade} anos')
print()