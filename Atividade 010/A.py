"""
A. Cadastro de frutas
Crie um conjunto contendo 4 frutas.
Depois, peça ao usuário para informar uma nova 
fruta que deseja cadastrar. Em seguida, peça uma 
fruta que deseja retirar do cadastro.

Ao final, exiba o conjunto atualizado.

Autor: Samuel Gurgel
Data: 19/08/2026
"""

frutas = {'maça','banana','laranja','uva'}

#adicionar uma fruta:
nova_fruta = input('Digite uma nova fruta para adicionar: ')
frutas.add(nova_fruta)

#remover uma fruta:
fruta_remover = input('Digite uma fruta para remover: ')
frutas.discard(fruta_remover)

print('Frutas cadastradas: ',frutas)