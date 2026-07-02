#aula-42-funcoes-4-escopo.py

"""
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir
Existe escopo global e local

O escopo global é o escopo onde todo código é alcançavel.
O escopo local é o escopo onde apenas nomes do mesmo local
podem ser alcançados.

"""
import os

#Exemplo 01
def escopo():
    x = 1 #escopo local
    print(x)

escopo()
#A variável 'x' neste caso, só existe no escopo dessa função
#print(x) #Isso daria um erro, pq 'x' não existe fora da função

#Exemplo 2:
y = 10 #escopo global
def escopo2():
    print(y)

escopo2()
#Neste bloco funcionaria pq o 'y' está no escopo global

#Exemplo 3:
def escopo3():
    print(z)

z = 5 #A variável precisa ser definida antes da execução da função
escopo3()

os.system('cls')
#Exemplo 4:
x = 999 #x global
def valor():
    global x #Estou informando que quero usar o 'x' global
    x = 60
    def valor2():
        x = 7
        print(x)
    print(x)
    valor2()

valor()
print(x)