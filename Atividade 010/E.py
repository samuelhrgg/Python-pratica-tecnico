"""
E. Festival de tecnologia 
Um festival ofereceu três palestras:
No festival foram realizadas três palestras:
python = {"Ana", "Carlos", "João", "Maria", "Pedro"}
ia = {"Carlos", "Maria", "Pedro", "Lucas", "Mariana"}
web = {"Ana", "Pedro", "Lucas", "Rafael"}

Crie um programa que:
- Mostre todas as pessoas que participaram de pelo menos uma palestra.
- Mostre quem participou somente de Python.
- Mostre quem participou de Python e IA.
- Mostre quem participou de apenas uma das três palestras.
- Verifique se todos os integrantes do grupo abaixo participaram 
   de pelo menos uma palestra:
grupo = {"Ana", "Carlos", "Maria"}

Autor: Samuel Gurgel
Data: 19/08/2026
"""
#Criando o SET
python = {"Ana", "Carlos", "João", "Maria", "Pedro"}
ia = {"Carlos", "Maria", "Pedro", "Lucas", "Mariana"}
web = {"Ana", "Pedro", "Lucas", "Rafael"}

#1. Todos que participaram de pelo menos uma palestra
todos = python.union(ia,web)

#2. Quem participou somente de Python
somente_python = python.difference(ia, web)

#3. Quem participou somente de Python e IA
python_ia = python.intersection(ia)

#4. Quem participou somente de uma paletra
#Forma 01
apenasUma = (
    (python-ia-web) | 
    (ia-python-web) |
    (web-python-ia)
)
#Forma 02
somente_ia = ia.difference(python,web)
somente_web = web.difference(python,ia)
apenas_uma = somente_python.union(somente_ia,somente_web)

#5.Verifica se todos do grupo participaram de pelo menos
#uma palestra
grupo = {"Ana", "Carlos", "Maria"}
participaram = grupo.issubset(todos)

print('Todos: ', todos)
print('Somente python: ',somente_python)
print('Python e IA: ',python_ia)
print('1º Apenas uma palestra: ',apenas_uma)
print('2º Apenas uma palestra: ',apenasUma)

if participaram:
    print('Todos membmros do grupo participaram')
else:
    print('Um ou mais membros do grupo não participaram')


