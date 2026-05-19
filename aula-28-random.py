#aula-28-random.py
"""
Biblioteca random

A biblioteca random em Python é uma biblioteca padrão que 
fornece funções para gerar números aleatórios e realizar operações 
relacionadas à aleatoriedade. Essa biblioteca é útil em uma variedade 
de aplicações, como simulações, jogos, criptografia, entre outros, 
onde a aleatoriedade desempenha um papel importante.

A função mais comum da biblioteca random é a função random(), 
que gera um número decimal aleatório entre 0 e 1 (inclusive 0, 
mas exclusivo de 1).

Isso significa que o número gerado pode estar em qualquer lugar
dentro do intervalo semiaberto [0, 1]).

"""
import random
import os

os.system('cls')

print('-'*70)
numeroAleatorio = random.random()
print(f'O número aleatório gerado é: {numeroAleatorio}')
print()

#randint(a,b) → Retorna um número inteiro aleatório entre a e
#  b(inclusive ambos limites)

#uniform(a,b) → Retorna um número decimal aleatório entre a e b
#  (inclusive ambos os limites), com uma distribuição uniforme.

#randrange(start, stop, step)
#Retorna um elemento aleatório de uma sequência gerada pela função 
# range(), começando em start, terminando antes de stop, e avançando
#  de acordo com step.

#choice(seq) → Retorna um elemento aleatório de uma sequência (como uma lista,
#tupla ou string)

#shuffle(seq) → Embaralha os elementos de um sequência

#sample(population, k) → Retorna uma amostra de k elementos únicos de uma
#população (sem substituição)