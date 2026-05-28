#aula-34-while.py

# Código → 774
# Limite: 19:47
"""
Repetições
Introdução While (enquanto)
Executa uma ação enquanto uma condição for verdadeira
"""
condicao = True

while condicao: #enquanto a condição for verdadeira
    # print(1)
    # print(2)
    # print(3)
    nome = input('Informe seu nome: ')

    if nome == 'sair':
        break #interromper o laço.
    
    else:
        print(f'Seu nome é {nome}')
    
print('Saiu do enquanto.')
