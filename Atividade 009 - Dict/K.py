"""
K.Faça um programa que peça continuamente o nome e a idade de 
uma pessoa. Caso o usuário digite a idade 999, o programa será
finalizado e executará uma impressão com os nomes e idades
cadastrados.

Autor: Samuel Gurgel
Data: 15/07/26
"""

cadastros = []

while True:
    nome = input('Nome: ')
    idade = int(input('Idade: '))

    if idade == 999:
        print('Encerrando o cadastro...')
        break

    pessoa = {
        'nome' : nome,
        'idade' : idade
    }
    cadastros.append(pessoa)

print('-' * 30)
print('Pessoas Cadastradas')

for pessoa in cadastros:
    print(f'Nome: {pessoa['nome']} | Idade: {pessoa['idade']}')