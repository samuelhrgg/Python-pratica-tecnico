#aula-36-list-15-in-not-in.py
"""
Saída com IN e NOT IN
"""
import os
os.system('cls')

print('-'*70)
print('Saída com IN e NOT IN')
print('-'*70)

#EXEMPLO COM IN
listaNumeros = [1,2,3,4,5,6,7,8,9,10]

if (3 in listaNumeros):
    print(listaNumeros)
    posicao = listaNumeros.index(3)
    print(f'O número 3 está na posição {posicao}')
else:
    print('O elemento não consta na listagem')
print()

#EXEMPLO COM NOT IN
listaNomes = ['Samuel','Fabio','Rodrigo']

if('Maria' not in listaNomes):
    print(listaNomes)

    #Não está na lista, vamos acrescentar:
    listaNomes.append('Maria')

    print(f'O nome Maria foi acrescentado na lista!')
    print(listaNomes)

else:
    print('O nome Maria já consta na lista!')

print('-'*70)