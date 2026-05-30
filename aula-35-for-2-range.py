#aula-35-for-2-range.py
"""
O comando for com range() em Python é uma maneira conveniente
de gerar uma sequência de números em um loop for.

A função range() gera uma sequência de números inteiros,
que podem ser usados como índices ou valores em um loop for.

Sintaxe for range:
for i in range(start, stop, step)

→ começa no início.
→ termina antes do fim.
"""

import os
os.system('cls')
print('-'*70)
print('ESTRUTURA DE CONTROLE FOR RANGE')
print('-'*70)
print()

for qualquerCoisa in range(1,8): #inicio de 1 até 7
    print(f'Valor: {qualquerCoisa}') #oculta o último índice do range

print()

#outra forma
inicio = 1
fim = 8
passo = 2

for iteravel in range(inicio,fim,passo):
    print(f'Valor: {iteravel}', end= ' | ')

print()
print()