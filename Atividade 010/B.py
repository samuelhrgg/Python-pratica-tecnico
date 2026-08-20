"""
B. Controle de participantes
Uma atividade possui os seguintes participantes:
turma = {"Ana", "Carlos", "João", "Maria", "Pedro"}
João não poderá mais participar da atividade.
Remova João e, depois, tente remover "Lucas", 
que não está cadastrado.

O programa não deve apresentar erro

Autor: Samuel Gurgel
Data: 19/08/2026
"""

turma = {"Ana", "Carlos", "João", "Maria", "Pedro"}

turma.remove('João') #Irá apagar pq existe.
turma.discard('Lucas') #Não apresentará erro.

print('Participantes: ', turma)