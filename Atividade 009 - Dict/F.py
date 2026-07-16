"""
F. Faça um programa que cadastra 5 tipos de vinho. 
Para os campos deste cadastro tome como referência nome do vinho,
tipo, teor alcoólico e safra.

Autor: Samuel Gurgel
Data: 15/07/26
"""
vinhos = {}

for i in range(1,6):
    print(f'Cadastro do Vinho {i}')
    nome = input('Nome: ')
    tipo = input('Tipo: ')
    teor = input('Teor: ')
    safra = input('Safra: ')

    vinhos[nome]={
        'tipo' : tipo,
        'teor' : teor,
        'safra' : safra
    }
print('Vinhos Cadastrados')

for nome,dados in vinhos.items():
    print(nome,dados)
