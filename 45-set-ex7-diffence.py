'''
difference() retorna um novo set com elemetos do primeiro ser que não estão no segundo set
'''
import os
os.system('cls')

print('Listagem de guerreiros so senac')

#criando set
set1 = {'Davi', 'Julio','Xandão', 'Arthur', 'Eduardo', 'Bruno', 'Fabio', 'FabioJr', 'Chico', 'Frankão', 'Gleisson', 'Gustavo', 'Jenifer', 'Jesiel', 'Jessica', 'JoãoPai', 'Jão67', 'Josue', 'Julia', 'Juliana', 'Kaio', 'LauroJr', 'Maria', 'Pedro'}
print(f'Guerreiros escolhidos → {set1}')

#usar o 'difference para remover os guerreiros abatidos nessa grande guerra
sobreviventes = set1.difference('Xandão','Bruno', 'Fabio', 'Gleisson', 'Gustavo', 'Jenifer', 'Jessica', 'JoãoPai', 'Josue', 'Julia', 'Juliana', 'Kaio', 'LauroJr', 'Maria')
print(f'Guerreiros sobreviventes na guerra → {sobreviventes}')
print(set1)