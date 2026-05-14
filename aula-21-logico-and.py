#aula-21-logico-and.py
"""
Operadores Lógicos
and (e) , or (ou) , not (não)
and → Todas as condições precisam ser verdadeiras.
Se qualquer valor for considerado falso, a expressão inteira será
avaliada naquele valor.

São considerados falso → 0, 0.0, '', False
Também existe o tipo None que é usado para representar um não valor.
"""

print()
entrada = input('[E]ntrar [S]air: ')
senha = input('Senha: ')
senhaCorreta = '123456'

if (entrada == 'E' and senha == senhaCorreta):
    print('Entrar')

else:
    print('Sair')

print()


#Avaliação de curto circuito
print(True and False and True) #(V e F e V) → (F e V) → (F)
print(True and False or True) #(V e F ou V) → (F ou V) → (V)
print(True and 0 and True)
print(bool(0))

