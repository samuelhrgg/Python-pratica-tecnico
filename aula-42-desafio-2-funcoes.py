#aula-42-desafio-2-funcoes.py

import os

def cls():
    os.system('cls')

cls()

def linha(x):
    print('-'*x)

# ----------- Funções ----------
def menu():
    linha(50)
    print(' URNA ELETRÔNICA')
    linha(50)
    print('10 - Ana')
    print('20 - Bruno')
    print('30 - Carlos')
    print('0 - Branco')
    print()
    print('1 - Exibir resultado')
    print('2 - Encerrar votação')
    linha(50)

def registrarVoto(voto,ana,bruno,carlos,branco,nulo):

    if voto == 10:
        ana += 1
    
    elif voto == 20:
        bruno += 1
    
    elif voto == 30:
        carlos += 1
    
    elif voto == 0:
        branco += 1
    
    else:
        nulo += 1

    return ana,bruno,carlos,branco,nulo

def resultado(ana, bruno, carlos,branco, nulo):

    total = ana + bruno + carlos + branco + nulo
    linha(50)
    print('Resultado da Votação')
    linha(50)

    print(f'Ana: {ana} voto(s)')
    print(f'Bruno: {bruno} voto(s)')
    print(f'Carlos: {carlos} voto(s)')
    print(f'Brancos: {branco} voto(s)')
    print(f'Nulos: {nulo} voto(s)')

    print(f'Total de votos: {total} voto(s)')
    linha(50)

    maior = max(ana,bruno,carlos)

    if maior == 0:
        print('Nenhum candidato recebeu votos!')
    
    elif(ana == bruno == maior) or (ana == carlos == maior) or (bruno == carlos == maior):
        print('A eleição terminou empatada!')
    
    elif maior == ana:
        print('Vencedora: Ana')

    elif maior == bruno:
        print('Vencedor: Bruno')
    
    else:
        print('Vencedor: Carlos')


# ----------- Programa principal ----------
ana = 0
bruno = 0
carlos = 0
branco = 0
nulo = 0

while True:
    menu() #chamando o menu

    try:
        opcao = (int(input('Digite seu voto ou escolha uma opção: ')))
    except:
        print('Entrada inválida!')
        input('Pressione ENTER...')
        cls()
        continue #volta no inicio do laço (while)

    if opcao == 1:
        resultado(ana,bruno,carlos,branco,nulo)
        input('Pressione ENTER para continuar...')
        cls()
    
    elif opcao == 2:
        print('Encerrando o sistema')
        resultado(ana,bruno,carlos,branco,nulo)
        break

    else:
        ana, bruno, carlos, branco, nulo = registrarVoto(
            opcao,
            ana,
            bruno,
            carlos,
            branco,
            nulo

        )
        print('Voto registrado com sucesso!')
        input('Pressione ENTER para continuar')
        cls()






