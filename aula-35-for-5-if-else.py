#Estrutura for com if e else

import os
os.system('cls')
linha = ('-'*50)

print(linha)
print('Estrutura FOR com IF e Else')
print(linha)

for x in range(0,4):
    numero = int(input(f'Informe o {x+1}º número: '))

    if (numero % 2 == 0):
        print(f'O número {numero} é par')
    else:
        print(f'O número {numero} é ímpar')
    
print(linha)
print()