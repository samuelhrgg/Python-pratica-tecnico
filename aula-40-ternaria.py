#aula-40-ternaria.py
"""
Ternária é uma forma de expressar uma condição de maneira
mais compacta. Ela é composta por três partes:
a condição, o valor se a condição for verdadeira e o 
valor se a condição for falsa.

Sintaxe:
valor = valorVerdadeiro if condicao else valorFalso
"""
idade = 18
status = 'Maior de idade' if idade >= 18 else 'Menor de idade'
print(status)

#outro exemplo
condicao = 10==5
variavel = 'verdadeiro' if condicao == True else 'Falso'
print(variavel)

#outro exemplo
digito = 8
novoDigito = digito if digito <= 9 else 0
print(novoDigito)

#outro exemplo
nome = 'pedro'
teste = 'samuel' if nome == 'samuel' else \
        'pedro' if nome == 'pedro' else 'outro nome'

print(teste)

print('x' if nome == 'samuel' else 'y')