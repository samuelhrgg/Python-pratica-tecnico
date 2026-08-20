"""
C. Duas turmas 
Uma escola possui duas turmas:
python = {"Ana", "Carlos", "João", "Maria"}
java = {"Carlos", "Pedro", "Maria", "Lucas"}
O programa deverá mostrar:
Todos os alunos que estão em pelo menos uma das turmas.
Os alunos que estão somente em Python.
Os alunos que estão somente em Java.
Os alunos que estão nas duas turmas.

Autor: Samuel Gurgel
Data: 19/08/2026
"""

python = {"Ana", "Carlos", "João", "Maria"}
java = {"Carlos", "Pedro", "Maria", "Lucas"}

#Todos os alunos
todos = python.union(java)

#Somente Python
somente_python = python.difference(java)

#Somente Java
somente_java = java.difference(python)

#Nas duas turmas:
nas_duas = python.intersection(java)

print('Todos: ', todos)
print('Somente python: ',somente_python)
print('Somente Java: ', somente_java)
print('Nas duas turmas: ',nas_duas)


