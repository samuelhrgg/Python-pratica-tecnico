#aula-35-for-6-break.py

import os

os.system('cls')

linha = ('-'*50)

print(linha)
print('ESTRUTURA DE CONTROLE FOR COM BREAK')
print(linha)

print()
for c in range(0,11):
    print(f'Valor: {c}')

    #Condição para parar a contagem:
    if (c == 5):
        print(f'Contagem interrompida no {c}')
        break

print(linha)
print('Fim')
print()
