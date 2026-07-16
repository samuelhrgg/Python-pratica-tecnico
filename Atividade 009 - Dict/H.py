"""
Faça um programa para ler o dicionário 
nomes = {‘nome’: ’John, ‘idade’: 40, ‘peso’: 80, ‘altura’: 1.70}.
Em seguida realize as seguintes ações:
- Listar chaves e valores com laço - Deletar o peso
- Listar novamente chaves e valores - mostrar o nome e altura

"""

nomes = {
    "nome": "John",
    "idade": 40,
    "peso": 80,
    "altura": 1.70
}

print('Dicionário original')
for chave, valor in nomes.items():
    print(chave, ':' , valor)

nomes.pop('peso')
print('-'*50)

print('Dicionário após remover o peso')
for chave, valor in nomes.items():
    print(chave, ':' , valor)

print('-'*50)
print('Nome: ',nomes['nome'])
print('Altura: ',nomes['altura'])
