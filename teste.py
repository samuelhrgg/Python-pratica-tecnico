#Calculadora com While

"""
Solicitar primeiro e segundo número, após isso
pedir o operador (+ , - , * , /)

Usuário decide quando parar

Utilize boas práticas para realizar validações e garantir
o bom funcionamento do programa.
"""

import os
import operator
os.system('cls')


continuar = True

while continuar:
    valor1 = input('Informe o primeiro valor: ')
    valor2 = input('Informe o segundo valor: ')
    
    try:
        valorVerificado1 = float(valor1)
        valorVerificado2 = float(valor2)
        numerosValidos = True
    except:
        numerosValidos = None
    
    if numerosValidos is None:
        print('Um ou ambos números são inválidos')
        continue

    operador = input('Informe o operador [+] [-] [*] [/]: ')
    operadoresPermitidos = '+-*/'

    if operador in operadoresPermitidos:

        if operador == '+':
            resultado = valorVerificado1 + valorVerificado2

        elif operador == '-':
            resultado = valorVerificado1 - valorVerificado2
        
        elif operador == '*':
            resultado = valorVerificado1 * valorVerificado2
        
        elif operador == '/':
            if (valorVerificado1 == 0) or (valorVerificado2 ==0):
                resultado= 'Operação inválida'
                
            else:
                resultado = valorVerificado1 / valorVerificado2

        else:
            resultado = 'Operação Inválida!'

        #biblioteca operator
        # operacoes = {
        # '+': operator.add,
        # '-': operator.sub,
        # '*': operator.mul,
        # '/': operator.truediv
        # }

        # resultado = operacoes[operador](valorVerificado1, valorVerificado2)
        
    else:
        resultado = 'Operação Inválida!'
        
    print(f'O resultado da operação é : {resultado}')

    while continuar:
        opcao = input('\nDesejar continuar: [S]im ou [N]ão: ')
        if opcao.lower() == 's':
            break
        elif opcao.lower() == 'n':
            continuar = False
        else:
            print('Operação inválida, informe S ou N')
    
    os.system('cls')

print('Programa Encerrado!')