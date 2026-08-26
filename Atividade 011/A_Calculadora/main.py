#Autor: Samuel Gurgel
#Data: 19/08/2026
#Lista 011 - Atividade A

# Peça dois números.
# Mostre um menu de operações.
# Importe as funções de operacoes.py.
# Execute a operação escolhida.
# Mostre o resultado.

#from operacoes import div,multi,somar,subtrair (1º jeito)
from operacoes import * #(2º jeito)

print('Calculadora')
print('Opções')
print('[1] - Somar')
print('[2] - Subtrair')
print('[3] - Multiplicar')
print('[4] - Dividir')
print('[0] - Sair')

n1 = float(input('Informe o primeiro número: '))
n2 = float(input('Informe o segundo número: '))

opcao = input('Informe a operação desejada: ')

if opcao == '1':
    print(f'Soma de {n1} + {n2} = {somar(n1,n2)}')

elif opcao == '2':
    print(f'Subtração de {n1} - {n2} = {subtrair(n1,n2)}')

elif opcao == '3':
    print(f'Multiplicação {n1} * {n2} = {multi(n1,n2)}')

elif opcao == '4':
    print(f'Divisão de {n1} / {n2} = {div(n1,n2)}')

elif opcao == '0':
    print('Encerrando o programa...')

else:
    print('Opção inválida, programa encerrado.')




