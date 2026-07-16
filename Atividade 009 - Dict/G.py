"""
G.Faça um programa para cadastrar os alunos de uma escola. 
Para os campos, tome como referência o nome do aluno, 
data de nascimento e matrícula

Autor: Samuel Gurgel
Data: 15/07/26
"""
import os
os.system('cls')

alunos = []

while True:
    try:
        quantidade = int(input('Quantidade a cadastrar: '))
        break
    except:
        print('Valor inválido')
        continue
        


for x in range(quantidade):

    aluno = {}
    print(f'Cadastro {x+1}º aluno:')
    aluno['nome'] = input('Nome do aluno: ')
    aluno['matricula'] = input('Matrícula: ')
    aluno['DataNascimento'] = input('Nascimento: ')

    alunos.append(aluno)

print()
i = 1

for x in alunos:
    print('-'*30)
    print(f'{i}º aluno:')
    i += 1
    for chave,valor in x.items():
        print(f'{chave} | {valor} ')
    

    




