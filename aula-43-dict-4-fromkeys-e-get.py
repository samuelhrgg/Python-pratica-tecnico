#aula-43-dict-4-fromkeys-e-get.py
"""
O método fromkeys() serve para criar um dicionário rapidamente, 
quando você já sabe quais serão as chaves e quer que todas elas
comecem com o mesmo valor.

Sintaxe: fromkeys(iterable, value=None)

get(key, default=None)
Retorna o valor para a chave se a chave estiver no dicionário
caso contrário, retorna default.
"""
import os
os.system('cls')

def linha(x):
    print('-' * x)

linha(50)
#Exemplo 01
print('Exemplo FROMKEYS:')
alunos = ['Ana','Carlos','Maria']

notas = dict.fromkeys(alunos,0)
print(notas)

#Exemplo 02
linha(70)
dias = ['Seg','Ter','Qua','Qui','Sex']
presenca = dict.fromkeys(dias,False)
print(presenca)
#alterar apenas uma chave
presenca['Ter'] = True
print(presenca)
linha(70)

#Exemplo 03

pupilos = {
    'Ana' : 8,
    'Carlos' : 9,
    'Maria' : 10
}
novo = dict.fromkeys(pupilos,0)
print(pupilos)
print(novo)

linha(70)

#======================= 
# Exemplo GET

aluno = {
    'nome' : 'João',
    'idade' : '20',
    'cidade' : 'Muriaé'
}

#print(aluno['cidade']) #Isso irá acarretar em um 'key error'
print(aluno.get('cidade')) #sem valor padrão
print(aluno.get('cidade','Cidade não existe!')) #com valor padrão
linha(70)

#Exemplo prático
if aluno.get('cidade') is not None: # se ele não for None
    print(f'Cidade existe!')

else:
    print(f'A cidade não foi encontrada')

#Exemplo completo
linha(70)
meu_dicionario = None

while True:
    linha(70)
    print('Menu de Opções')
    print('1 - Criar dicionário com fromkeys()')
    print('2 - Buscar valor de uma chave com get()')
    print('3 - Sair')
    linha(70)

    opcao = input('Escolha uma opção de (1-3): ')

    if opcao == '1':
        #Criação de um dicionário usando fromkeys()
        chaves = input('Digite as chaves, separadas por vírgula: ').split(',')
        valor_padrao = input('Digite o valor padrão para todas as chaves: ')
        meu_dicionario = dict.fromkeys(chaves,valor_padrao)
        print(f'Dicionário criado: {meu_dicionario}')
    
    elif opcao == '2':
        #Verificar se o dicionário foi criado antes de tentar acessa-lo
        if meu_dicionario is not None:
            chave = input('Digite a chave que deseja buscar: ')
            valor = meu_dicionario.get(chave,'Chave não encontrada')
            print(f'Valor para a chave: "{chave}" : "{valor}"')
        
        else:
            print('Erro!,Crie um dicionário')
    
    elif opcao == '3':
        print('Saindo do programa')
        break

    else:
        print('Opção inválida, tente novamente!')
