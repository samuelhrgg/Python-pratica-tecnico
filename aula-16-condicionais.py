#Conhecendo as condições e blocos de código no Python
#(If / elif / else ) → (se / senão se / senão)

print()
entrada = input('Você quer "entrar" ou "sair": ')

#se entrada for igual à 'entrar'
if entrada == 'entrar': #verificando se é verdadeiro
    print('Você entrou!')

elif entrada == 'sair': #senao se fazendo outra verificação
    print('Você saiu!')

else: #senão
    print(f'Você digitou {entrada}.')

print('Fora do bloco')

