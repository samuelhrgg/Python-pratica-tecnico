#aula-35-for-7-continue.py

import os
os.system('cls')

linha = ('-'*70)

print(linha)
print('ESTRUTURA DE CONTROLE: CONTINUE')
print(linha)

print()
for x in range(1,11):
    if x == 5:
        #print(f'O número {x} está fora do loop.')
        continue

    print(f'Número: {x}')

print(linha)
print()