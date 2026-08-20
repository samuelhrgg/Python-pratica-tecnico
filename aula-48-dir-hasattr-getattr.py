#aula-48-dir-hasattr-getattr.py
#dir, hasattr e getattr

import os

os.system('cls')

string = 'Samuel'
metodo = 'upper'

print(string)

teste = hasattr(string, 'lower')
print(teste)

teste = hasattr('feijão','lower')
print(teste)

teste = hasattr(string,metodo)
print(teste)

print('-'*70)

if hasattr(string,metodo): #verifica se existe o método, poderia passar direto ('upper')
    print('Existe Upper')
    #print(string.metodo()) #não funciona
    print(getattr(string,'upper')()) #1º forma executa o método
    print(getattr(string,metodo)()) #2º forma executa o método

else:
    print('Não existe o método ', metodo)
