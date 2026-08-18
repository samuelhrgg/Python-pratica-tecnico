"""
Metodo set {}
Usando o clear e o issubset(set2) 

Clear:

O método clear() é usado quando você deseja esvaziar completamente um set, 
removendo todos os seus elementos, mas mantendo a variável existente.

Use clear() quando você quiser reaproveitar o mesmo conjunto, apagando todos os dados armazenados nele. 
Isso é útil, por exemplo, quando um programa precisa limpar informações antigas antes de adicionar novos elementos.

Dica: clear() é diferente de remove(). Enquanto remove() 
apaga apenas um elemento específico, clear() apaga todos os elementos do conjunto de uma só vez.

Sintaxe:

set.clear()
------------------
issubset(set2):

O método issubset() é usado para verificar se todos os elementos de um conjunto (set) estão contidos em outro conjunto.

Em outras palavras, ele responde à pergunta:

"Este conjunto é um subconjunto do outro?"

Ele retorna:

True → se todos os elementos do primeiro conjunto existem no segundo.
False → se pelo menos um elemento não existir.

Sintaxe

set1.issubset(set2)

"""

#Criação do "SET"


planetas = {'Terra', 'Vênus', 'Mercurio', 'Marte'}

#Usando a função clear()
print('Antes: ',planetas)

planetas.clear()

print('Depois: ', planetas)

#Usando a função  "issubset"

print('-'*30)

#Criar o segundo set para comparação

planetas_2 = {'Saturno', 'Plutão', 'Mercurio', 'Marte', 'Terra', 'Vênus'}

print(planetas.issubset(planetas_2)) #Verificar se os elementos do primeiro conjunto está no segundo conjunto, retorna True

print('-'*30)
print('Removendo 1 item do primeiro conjunto: ')
planetas_3 = {'Saturno', 'Plutão', 'Mercurio', 'Marte', 'Terra'} #Removendo o ultimo item
print(planetas_2.issubset(planetas_3)) #Verificar se os elementos do primeiro conjunto está no segundo conjunto, retorna False caso falte algum item









