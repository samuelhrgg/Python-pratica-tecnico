#aula-32-introducao-try-except.py
"""
Introdução ao Try e Except no Python
try → tenta executar um código
except → caso ocorra um erro ao tentar executar ele faz outra 
parte do código

"""
print(1234)
print(123)
#int('a')

numeroStr = input('Digite um valor para descobrir o dobro: ')

#tratar o input que o usuário irar digitar.
try:
    numFloat = float(numeroStr)
    print(f'{numFloat * 2}')

except:
    print(f'Isso não é um número')

