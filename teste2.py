import os
os.system('cls')

print('-' * 70)
print('Funções para Lista: EXTEND')
print('=' * 70)

#Juntando duas listas
print('Utilizando o Extend')
listaA = [1,2,3]
listaB = [4,5,6]
listaC = listaA + listaB
print(f'Nova lista: {listaC}')

#utilizando o extend
listaA.extend(listaB)
#EXTEND não retorna nada, mas realizou a mudança na lista A

#o extend trabalha diretamente na lista A
print(f'Nova lista A: {listaA}') 
print(f'Lista B: {listaB}')
print()
print('-'*70)