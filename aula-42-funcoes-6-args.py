#aula-42-funcoes-6-args.py
"""
args - Argumentos não nomeados
* (empacotamento e desempacotamento)
"""

#Relembrando empacotamento
x, y, *resto = 'a','b','c','d','e','f','g'
print(x,y,resto)

def valores(*args): #boa prática utilizar o termo 'args'
    return(args)

print(valores(1,2,3,4,5,6,7,8,9,10))

def sub(*args):
    return('nada')

print(sub(1,2,3))

def somar(*args):
    total = 0
    for numero in args:
        total += numero
    return total

print(somar(20,20,20,20,20))
outraSoma = somar(5,5,5)
maisUmaSoma = somar(2,2,2)
print(outraSoma)
print(maisUmaSoma)

numeros = 1,2,3,4,5,6
soma2 = somar(*numeros)
print(soma2)

