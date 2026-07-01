#aula-42-funcoes-1.py
"""
Introdução as funções (def) em Python
Função são trechos de código usados para replicar 
determinadas ações ao longo do seu código.

Elas podem receber valores em parâmetros e podem
retornar valores para serem usados em outras partes do 
código

Por padrão, função não retornam valores, retornam 
None(nada). Para retornar valores, usamos a palavra
reservada 'return'.
"""

import os
os.system('cls')

print('Função de Print')

def Print(): #define uma função
    print('Nova função')
    print('Nova função')
    print('Nova função')

Print()

#A ideia da função é replicar ações
def linha():
    print('-'*30)

linha()

#Função recebendo valores:
def imprimir_valores(a, b, c): #a,b, c são parâmetros da função
    print(f'Valores recebidos: {a}, {b}, {c}')

imprimir_valores(10,20,30) #10, 20, 30 são argumentos da função
imprimir_valores(5,6,7)

def par_impar(numero):
    if numero % 2 == 0:
        print(f'O número {numero} é par')
    else:
        print(f'O número {numero} é impar')

par_impar(10)

valor = int(input('Informe um valor: '))
par_impar(valor)
linha()

#Valor padrão
#caso nada seja passado, será usado esse valor padrão
def saudacao(nome='Usuário'): 
    print(f'Olá {nome}, seja bem-vindo(a)!')


saudacao('João')
saudacao('Maria')
saudacao('Arthur')
saudacao()



