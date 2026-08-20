"""
D. Equipe de projeto 
Uma empresa possui todos os funcionários cadastrados:
funcionarios = {"Ana", "Carlos", "João", "Maria", "Pedro", "Lucas"}
Para um projeto, foi formada uma equipe:
equipe = {"Ana", "João", "Maria"}
O programa deve verificar se todos os integrantes 
da equipe fazem parte da empresa.

Depois, João deixa a equipe e Carlos entra no projeto.
Atualize os dados e faça novamente a verificação.

Autor: Samuel Gurgel
Data: 19/08/2026
"""

funcionarios = {"Ana", "Carlos", "João", "Maria", "Pedro", "Lucas"}
equipe = {"Ana", "João", "Maria"}

#Verifica se todos da equipe são funcionários
if equipe.issubset(funcionarios):
    print('Todos fazem parte da equipe!')
else:
    print('Um ou mais não fazem da equipe')

#João sai e Carlos entra na empresa
equipe.remove('João') 
equipe.add('Carlos')

print('Nova equipe: ',equipe)

#Verifica novamente:
#Verifica se todos da equipe são funcionários
if equipe.issubset(funcionarios):
    print('Todos fazem parte da equipe!')
else:
    print('Um ou mais não fazem da equipe')
