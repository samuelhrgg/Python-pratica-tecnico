#aula-22-logico-or.py
"""
Operadores Lógicos
and (e) , or (ou) , not (não)
or → Qualquer condição verdadeira avalia toda a expressão como verdadeira

"""

print()
entrada = input('[E]ntrar [S]air: ')
senha = input('Senha: ')
senhaCorreta = '123456'

#Se a 'entrada' for 'E' ou 'e', e a senha for a senha correta!
if ((entrada == 'E'or entrada == 'e') and senha == senhaCorreta):
    print('Entrar')

else:
    print('Sair')

print()


#Avaliação de curto circuito
print(True or False) #verdadeiro ou falso? → verdadeiro
print(True and False or True) 
print((True or False) and False) #primeiro exemplo


#Atalho Comentar bloco: Seleciona bloco → Ctrl+k → Ctrl+C
#Atalho Descomentar Bloco: Seleciona bloco → Ctrl+k → Ctrl+u
#Atalho 2 → Shift + alt + A