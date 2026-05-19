#aula-29-random-exemplos.py

import os
import random
import time

os.system('cls')

linha = '-'*70
print(linha)
print('Biblioteca Random')
print(linha)

#Random
print('Número aleatório decimal entre 0 e 1')
numeroAleatorio = random.random()
print(f'O número gerado foi {numeroAleatorio}')
print(linha)

#Randint
print('Número aleatório Inteiro entre x e y')
aleatorioInteiro = random.randint(1,20)
print(f'O número inteiro gerado foi: {aleatorioInteiro}')
print(linha)

#Uniform
print('Número aleatório decimal em um intervalo')
aleatorioDecimal = random.uniform(1,20)
print(f'O número decimal gerado foi: {aleatorioDecimal}')
print(linha)

#Choice
print('Sorteio em uma lista')
lista = ['Ágata', 'Coly', 'Isis', 'Bia']
nomeSorteado = random.choice(lista)
print(f'Lista: {lista}')
print(f'O nome escolhido foi: {nomeSorteado}')
print(linha)

#Shuffle
print('Embaralhar uma sequência')
lista2 = ['Pedro','Tiago','João','Barquinho']

print(f'Lista antiga: {lista2}')
random.shuffle(lista2)
print(f'Lista nova: {lista2}')
print(linha)

#Sample
print('Retorno de elementos únicos de uma população: ')
numeros = [1,2,3,4,5,6,7,8,9]
amostraAleatoria = random.sample(numeros,5)
print(f'Retorna da amostragem: {amostraAleatoria}')
print(linha)

#Randrange
intervalo = random.randrange(0,20,2)
print(f'O número escolhido foi: {intervalo}')

print('Aguarde 5 segundos')
time.sleep(5)
print('Agora mostra isso!')