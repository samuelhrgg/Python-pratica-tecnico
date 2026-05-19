"""
F#) A empresa "LeapYearCheck" está desenvolvendo um 
software de verificação de anos bissextos para auxiliar usuários na 
identificação desses anos de forma rápida e precisa. 
Eles precisam de um programa que permita aos usuários inserir um ano e,
em seguida, determine se esse ano é bissexto ou não, de acordo com as
regras estabelecidas pelo calendário gregoriano. Além disso, é necessário 
realizar a validação de entrada de dados para garantir que o ano inserido 
pelo usuário seja um valor válido, ou seja, um número inteiro positivo.

Curso: Técnico em Desenvolvimento de Sistemas - Senac Minas
Aluno: Samuel Gurgel
Docente: Samuel Gurgel
Data: 13/05/2026

"""
ano = int(input('Informe um ano: '))

if ano <= 0:
    print('Ano inserido inválido!')

elif (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f'O ano {ano} é ano bissexto!') 

else:
    print('O ano não é bissexto')