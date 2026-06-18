#aula-39-desempacotamento.py
"""
Desempacotamento é o processo de atribuir os elementos de um iterável
a variáveis individuais. 

O desempacotamento é útil quando você deseja extrair valores de uma lista,
tupla ou qualquer outro itéravel e atribu-los a variáveis
separadas. Por exemplo, se você tiver uma tupla ccom três elementos
pode desempacotá-la em três diferentes variáveis. 

"""
string = 'ABCD'
lista = ['Pedro','Tiago','João','Barquinho']
tupla = ('Python','Java','C++')

a,b,c,d = string
print(a,b,c,d)

x,*resto,y = lista
print(x,y)
print(resto)

print(*resto)


#processamento de csv
linha = ['Samuel','27','Professor','Muriaé','MG']

nome,idade,*dados = linha
print()
print(f'Nome: {nome}')
print(f'Idade: {idade}')
print(f'Restante dos dados: {dados}')
