#aula-33-id-flags.py
"""
id = identidade
Flags (bandeiras) - marca um local
None = Não valor
is e is not = é ou não é um valor ''=='' / '!='

"""
v1 = 'a' #guardado na memória, o python busca esse elemento
print(id(v1))

v2 = 'a'
print(id(v2))

#Flags

passou = None

if passou is None:
    passou = True
    print('Passou')

else:
    passou = False
    print('Não passou')

