"""
B. Utilizando o exercício anterior,  
adicione mais 2 elementos ao dicionário.

Autor: Samuel Gurgel
Data: 15/07/26
"""
dados = {
    'nome' : 'Samuel',
    'idade' : 27,
    'cidade' : 'Muriaé',
    'profissao' : 'Professor'
}

dados['telefone'] = '(32)9999-9999'
dados.setdefault('Estado Civil','Casado')

print('Novo dicionário')
print(dados)
