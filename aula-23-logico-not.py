#aula-23-logico-not.py
"""
Operador lógico 'not'
Usado para inverter expressões

not True = False
not False = True
"""

print(not True)
print(not False)
print()

senha = input('Senha: ')

if not senha: #Verifica se a senha está vazia, pois algo vazio é considerado 'Falso'. 
    print('Você não digitou nada!')

elif senha == '123456':
    print('Entrou')

else:
    print('Senha Incorreta')




