#aula-42-funcoes-5-return.py

"""
Retorno de valores das funções (return)
"""
#Exemplo 01
variavel = print('Samuel')
print(variavel)
print('-' * 30)

#Exemplo 02
def soma(x,y): #parametros
    print(x+y)

variavelDois = soma(1,2)
print(variavelDois) #retornará None
print('-' * 30)

#Exemplo 03
def somando(x,y):
    resultado = x + y
    return resultado  #o return é a última coisa que a função faz
    print(1+1)
    
soma1 = somando(2,2)
soma2 = somando(3,3)
print(soma1,soma2)
print(soma1 + soma2)

