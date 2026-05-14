#aula-24-1-in-not-in.py
"""
Operadores in e not in
in → entre
not in → não está entre

Strings são iteráveis em Python.(Pode navegar item por item)

 S A M U E L #consegue navegar na string indice à indice
 0 1 2 3 4 5 #pode ser usado tanto indice positivo
-6-5-4-3-2-1 #pode ser usado índices negativos 

"""
nome = 'Samuel'
print(nome[2]) #Acessar o indice 2, letra 'm'
print(nome[-4]) #Acessar o índice -4, letra 'm'

#checando letra por letra com 'in'
print('m' in nome) #verificando se 'm' está entre as letras do nome
print('p' in nome) #verificando se 'p' está entre as letras do nome

#checando se não existe uma letra ou palavra com 'not in'
print('Sam' not in nome)
print('Ped' not in nome)

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar no nome: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')

else:
    print(f'{encontrar} não está em {nome}')