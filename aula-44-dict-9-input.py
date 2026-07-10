"""
Se os dados forem digitados pelo usuário, normalmente
criamos um dicionário para cada aluno e adicionamos em
uma lista.

"""
alunos = []
quantidade = int(input('Quantos alunos deseja cadastrar: '))

for x in range(quantidade):
    print(f'Cadastro do {x+1}º aluno: ')

    aluno = {}
    aluno['Nome'] = input('Nome: ')
    aluno['Idade'] = int(input('Idade: '))
    aluno['Nota'] = float(input('Nota: '))

    alunos.append(aluno)

print('Lista de alunos: ')
print(alunos)

#Imprimindo de forma bonita
i = 0
for x in alunos:
    print('-'*30)
    i += 1
    print(f'{i}º Aluno:')
    for chave, valor in x.items():
        print(f'{chave} - {valor} ')


