"""
Entrada de dados e comando Input

É importante observar que o valor retornado pelo comando input()
será sempre tratado como uma string, mesmo que o usuário digite um
número ou outro tipo de dado. Se você deseja utilizar outro formato,
deverá converter a str para int, float ou outro formato. 

"""
#mensagem = input('O que deseja falar para o mundo? ')
#print(f'{mensagem}, mundo!')

#1ª opcao
#numero1 = int(input('Digite um número: '))
numero1 = input('Digite um número: ')
#numero2 = int(input('Digite outro número: '))
numero2 = input('Digite outro número: ')

#2ª opcao
soma = int(numero1)+int(numero2)

#3ª opcao:
int_n1 = int(numero1)
int_n2 = int(numero2)
soma2 = int_n1+int_n2

print(f'A soma dos números é: {soma=}') #soma= trás o nome da variável o valor dela
print(f'A soma dos números é: {soma2}')


