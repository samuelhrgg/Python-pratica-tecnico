#aula-43-dict-8-for-py

def linha(x):
    print('='*x)
    print()

#Dicionário:
aluno = {
    'Nome ' : 'Samuel',
    'Idade' : 27,
    'Curso' : 'Python'
}
#Percorrendo somente as chave
for x in aluno:
    print(x)
linha(50)
#Mesma coisa ↓ 
for x in aluno.keys():
    print(x)
linha(50)

#2. Percorrendo somente os valores:
for valor in aluno.values():
    print(valor)
linha(50)

#3. Percorrendo chave e valor 
for x,y in aluno.items():
    print(f'Chave: {x} | Valor: {y}')
linha(50)

#4. E se eu tiver vários alunos?
alunos = [
    {
        'Nome' : 'Ana',
        'Idade' : 18,
        'Nota' : 90
    },

    {
        'Nome' : 'Carlos',
        'Idade' : 20,
        'Nota' : 75
    },

    {
        'Nome' : 'Maria',
        'Idade' : 20,
        'Nota' : '98'
    }
]

#Somente um for:
for aluno in alunos:
    print(aluno)
    #Cada repetição pega um dicionário inteiro

#Exibindo com dois for:
for aluno in alunos:
    print('-'*30)
    for chave, valor in aluno.items():
        print(f'Chave: {chave} - Valor: {valor}')
linha(50)

#Exibindo apenas os nomes:
for x in alunos:
    print(x['Nome'])
linha(50)