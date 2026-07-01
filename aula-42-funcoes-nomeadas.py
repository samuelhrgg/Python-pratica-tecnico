#aula-42-funcoes-nomeadas.py
"""
Argumentos nomeados e não nomeados em função Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado, é apenas o valor passado para a função
"""
import os

def limpar():
    os.system('cls')

limpar()

def soma(x,y): #soma recebe x,y no parametro
    #definição da função
    print(x+y)

soma(2,3) #argumentos

def soma_dois(x,y):
    print(f'{x=} + y={y} | Resultado: {x+y}')

soma_dois(5,10)

#Nomeando argumentos
soma_dois(y=20,x=5)

def multi(x,y,z):
    print(f'{x=} * {y=} * {z=} | Resultado: {x*y*z}')

multi(1,2,3) #argumentos não nomeados
multi(z=1, x=2, y=3) #argumento nomeados
multi(100,y=750,z=520) #exemplo nomeado e não nomeado
print('Olá',end='\n')

def porcentagem(x):
    resultado = ((x * 10) / 100)
    return resultado

variavel = porcentagem(10)
print(variavel)

#programa princpal
