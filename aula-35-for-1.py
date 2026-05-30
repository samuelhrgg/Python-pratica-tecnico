#aula-35-for-1.py

"""
Introdução ao FOR
O comando for em Python é uma estrutura de controle usada para
iterar sobre uma sequência de elementos. Ele executa um bloco
de código para cada item na sequência

Quando usar o For?
Quando já está determinado até quando o programa irá rodar uma
repetição.

While → Quando não se sabe quantas vezes o programa irá ter que
rodar uma repetição.

"""

#Exemplo
import os
os.system('cls')

texto = 'Python'
novoTexto = ''
tamanhoTexto = len(texto)
for letra in range(tamanhoTexto,4) : #para cada letra do texto
    novoTexto += f'*{letra}'
    print(letra)

#fora do for
print(f'{novoTexto}*')
