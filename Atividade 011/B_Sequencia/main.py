"""
O programa deverá apresentar um menu com as opções:
===== GERADOR DE SEQUÊNCIAS =====

1 - Sequência de 1 até X
2 - Números pares até X
3 - Números ímpares até X
0 - Sair

Ao escolher uma das opções, o usuário deverá informar um número X.
O programa deverá então gerar e apresentar a sequência correspondente.
Exemplo: se N = 10:
Sequência de 1 até N → 1 2 3 4 5 6 7 8 9 10
Números pares → 2 4 6 8 10
Números ímpares → 1 3 5 7 9

Modularização
No arquivo sequencias.py, crie uma função para cada tipo de sequência:
sequencia_ate_n()
pares_ate_n()
impares_ate_n()

O arquivo main.py deverá ser responsável pelo menu e pela interação com o usuário, 
importando e utilizando as funções criadas no módulo sequencias.py.

Regras
O programa deve continuar funcionando até que o usuário escolha 0 - Sair.
O usuário deve informar um número inteiro positivo.
Cada sequência deve ser gerada por uma função diferente.
As funções de geração das sequências devem ficar no arquivo sequencias.py.
O main.py deverá utilizar import para acessar as funções do outro arquivo.

Desafio extra: permita que o usuário escolha também o passo da sequência.
"""
import sequencia
from sequencia import impares_ate_n, pares_ate_n

final = int(input('Qual será o final da sequencia: '))

while True:

    print()
    print('\n===== GERADOR DE SEQUÊNCIAS =====',
            f'\n1 - Sequência de 1 até {final}',
            f'\n2 - Números pares até {final}',
            f'\n3 - Números ímpares até {final}',
            f'\n0 - Sair'
        )

    opcoes = ['1','2','3','0']
    opcao = input('Escolha uma opção: ')

    #Se a opção escolhida não estiver na lista de opcoes:
    if opcao not in opcoes:
        print('Opção inválida!')
        continue
    else:
        if opcao == '0':
            print('Encerrando o programa')
            break

        elif opcao == '1':
            passo = int(input('Qual será o passo do intervalo: '))
            sequencia.sequencia_ate_n(final,passo)

        elif opcao == '2':
            passo = int(input('Qual será o passo do intervalo: '))
            pares_ate_n(final,passo)

        elif opcao == '3':
            passo = int(input('Qual será o passo do intervalo: '))
            impares_ate_n(final,passo)

        else:
            print('Opção inválida!')
    
        
