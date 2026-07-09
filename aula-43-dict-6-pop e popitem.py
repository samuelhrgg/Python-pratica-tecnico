#aula-43-dict-6-pop e popitem.py
"""
pop() e popitem() em dicionários
pop(key, default=None)
→ Remove uma chave específica e retorna seu valor

popitem()
→ Remove e retorna o último par (chave,valor) do dicionário
"""

import os
os.system('cls')

aluno = {
    'Nome' : 'Samuel',
    'Idade' : 27,
    'Curso' : 'Python',
    'Nota' : 95
}

print('Lista atual: ', aluno)

#Metodo pop()
valor = aluno.pop('Nota')
print('Valor excluido: ',valor)
print('Lista atualizada: ',aluno)
print()

resultado = aluno.pop('Cidade','Cidade não existe!')
print('Elemento apagado: ',resultado)
print()
#Método popitem()
#Remover o último item que foi adicionado
print('Lista atual: ',aluno)
item = aluno.popitem()
print('Item removido: ',item)
print('Lista nova: ',aluno)
print()