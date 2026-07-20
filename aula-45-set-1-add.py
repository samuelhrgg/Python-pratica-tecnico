# 5,8,1 Add, union e symmetric_diferrence

import os
def limpa():
    os.system('cls')

total_alunos = set(['Francisco' , 'Frank' , 'Davi' , 'Julio' , 'Samuel'])

print ('Presente:' , total_alunos) 

faltantes = input('Qual aluno está faltando hoje? ')

total_alunos.add(faltantes)
total_alunos.add('Arthur')

print( total_alunos)