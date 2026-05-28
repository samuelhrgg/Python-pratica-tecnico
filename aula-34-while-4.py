#aula-34-while-4.py

"""
Iterando strings com While 

"""

# Leia o nome e exiba no 
# seguinte formato → *S*a*m*u*e*l* *G*u*r*g*e*l*
nome = input('Informe um nome: ')  #strings são iteráveis
novaString = ''
x = 0

while x < len(nome):
    novaString += '*' + nome[x]
    x += 1

    if x == len(nome):
        novaString += '*'

print(novaString)

print('-'*70)
#Arthur mode:
nomeNovo = 'Arthur'
juncao = '*'.join(nomeNovo)
print(f'*{juncao}*')