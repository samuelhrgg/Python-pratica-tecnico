#aula-35-for-3-input.py 
#Comando for .. range com input()

import os
os.system('cls')

print('-'*70)
print('ESTRUTURA DE CONTROLE FOR RANGE')
print('-'*70)

print()

for iteradora in range(1,5):
    cor = input(f'Digite a {iteradora}ª cor: ')
    if cor == 'amarelo':
        print('parabéns')

print(cor)
print()