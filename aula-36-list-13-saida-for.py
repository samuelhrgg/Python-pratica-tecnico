#aula-36-list-13-saida-for.py
"""
Imprimindo valores da lista com FOR

"""
import os
os.system('cls')

print('-'*70)
print('Saída com FOR')
print('-'*70)

listaFlores = []

#preencher 5 flores:
for x in range(0,5):
    flor = input(f'Informe o nome da {x+1}ª flor: ')
    listaFlores.append(flor)
print()
print('Saída das flores:')
print(f'Método simples: {listaFlores}')

#usando len para saber a quantidade de alunos:
for i in range(len(listaFlores)):
    print(listaFlores[i],end='/ ')
print()
print('-'*70)