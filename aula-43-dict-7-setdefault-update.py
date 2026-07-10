#aula-43-dict-7-setdefault-update.py

"""
O método setdefault() verifica se uma chave existe no dicionário.

Se a chave EXISTIR:
→ Apenas retorna o valor da chave

Se a chave NÃO EXISTIR:
→ Cria essa chave com valor informado

Sintaxe:
dicionario.setdefault(chave,valor)
"""
import os
os.system('cls')

def linha(x):
    print('-'*x)


aluno = {
    'Nome' : 'Samuel',
    'Idade' : '27',
    'Curso' : 'Desenvolvimento de Sistemas'
}
#Método setdefault()
print(aluno.setdefault('Nome','João'))
linha(30)

#Utilizando setdefault() com uma chave inexistente
print(aluno.setdefault("Cidade", "Muriaé"))
linha(30)

#=============== MÉTODO UPDATE ==============
#Update() → serve para atualizar um dicionário
#Ele pode, alterar valors ou adicionar novas chaves.
aluno.update({
    'Idade': 18,
    'Nota' : 10
})
print(aluno)
linha(30)

aluno.update({
    'Curso' : 'Python'
})
print(aluno)
linha(30)

#Update utilizando parametros()
aluno.update(Cidade = 'Cataguases' , Nota = 100)
print(aluno)
