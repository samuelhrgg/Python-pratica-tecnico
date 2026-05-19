"""
H#) A empresa "SecurePass" está desenvolvendo um novo sistema de 
cadastro de usuários para aumentar a segurança de sua plataforma digital.
Eles precisam de um programa em Python que solicite ao usuário a criação 
de uma senha e, em seguida, peça a confirmação dessa senha para 
garantir que ambas sejam iguais.

Além disso, por questões de segurança, o sistema exige que a senha 
contenha pelo menos um caractere especial, como: @, !, #, $, %, &, *

O programa deverá verificar:

Se a senha informada é igual à confirmação da senha;
Se a senha possui pelo menos um caractere especial válido.

Caso as senhas sejam diferentes, o programa deverá exibir uma 
mensagem informando o erro.

Caso a senha não contenha um caractere especial, o 
programa deverá alertar o usuário sobre essa exigência.Se todas as 
validações forem atendidas, o sistema deverá exibir uma mensagem 
confirmando que a senha foi cadastrada com sucesso.


Curso: Técnico em Desenvolvimento de Sistemas - Senac Minas
Aluno: Samuel Gurgel
Docente: Samuel Gurgel
Data: 13/05/2026

"""
print()
print('-'*20)
print('Verificação de Senha')

senha = input('Informe uma senha: ')
if not senha:
    print('Error, você não digitou nada!')

confirmeSenha = input('Confirme sua senha: ')

if senha != confirmeSenha:
    print('As senhas não são iguais!')

elif ('@' or '!' or "#" or '$' or '%' or '&' or '*') in senha:
    print('A senha deve conter um caracter especial!')

else:
    print('Senha cadastrada com sucesso!')

print()
