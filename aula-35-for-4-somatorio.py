#aula-35-for-4-somatorio.py
#Comando for range com somatório

import os
os.system('cls')

print('-'*70)
print('ESTRUTURA FOR COM SOMA')
print('-'*70)

soma = 0
for x in range(0,4):
    numero=int(input(f'Digite o {x+1}º valor: '))
    #calculo
    soma = soma + numero

print('-'*70)
print(f'A soma dos números é: {soma}')
print()
