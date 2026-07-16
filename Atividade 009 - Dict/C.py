"""
C. Utilizando o exercício anterior, retire um elemento do dicionário.


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


excluido = dados.pop('idade')
del dados['profissao']

print('Novo dicionário:')
print(dados)
