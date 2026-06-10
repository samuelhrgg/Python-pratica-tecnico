"""
Métodos/funções para listas: copy()

É usado para criar uma cópia rasa de uma lista. Uma cópia rasa
significa que a nova lista é uma cópia dos elementos da lista original,
mas, se os elementos forem objetos mutáveis, as mudanças nesses objetos
na nova lista também afetarão a lista original.

Sintaxe:
novaLista = listaOriginal.copy()


"""
import os
os.system('cls')

print('-'*70)
print(f'Funções para lista: COPY')
print('-'*70)

#Dados mutáveis
nome = 'Samuel'
outraVariavel = 'Samuel'
nome = 'João'
print(nome)
print(outraVariavel)

#listas
listaA = ['Samuel','Felipe']
listaB = listaA
#Qualquer alteração na lista A, impacta na lista B
listaA[0] = 'Outra coisa'
print(listaB)

#Dados imutáveis
#Ter duas listas com valores iguais porém distintas
listaD = ['Pedro','Tiago','João']
listaE = listaD.copy()

listaD[1] = 'Mateus'
print(listaE)
print(listaD)
