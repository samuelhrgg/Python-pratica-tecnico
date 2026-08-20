#Aula-46-set-revisao.py

frutas = {'maça','banana','laranja'}
outras = {'banana','uva','morango'}

#1. add() - adicionar
#Adiciona um elemento ao set.
frutas = {'maça','banana'}
print(frutas)
frutas.add('laranja')
print('Novo Set com elemento adicionado: ',frutas)

#2. remove() - remover
#Remove um elemento do set
frutas.remove('banana')
print('Novo Set com elemento removido: ',frutas)

#3. union() - união
#Junta os elementos de dois sets
resultado = frutas.union(outras)
print('Novo SET unido: ',resultado)

#4.Symmetric_difference() - diferença simétrica
#Retorna os elmentos que estão em um ou outro conjunto
#mas não em ambos.
frutas = {'maça','banana','laranja'}
outras = {'banana','uva','morango'}

resultado = frutas.symmetric_difference(outras)
print('SET com elementos distintos: ',resultado)

#5. discard() - remover
#Também remove um elemento, mas não acontece um erro
#caso o elemento não esteja presente no SET
frutas.discard('banana')
print('SET com elemento removido: ',frutas)

#6.difference() - diferença
#Mostra os elementos que estão no primeiro set,
#mas não no segundo
#'O que existe em frutas que NÃO existe em outras?'
frutas = {'maça','banana','laranja'}
outras = {'banana','uva','morango'}
resultado = frutas.difference(outras)
#resultado = frutas - outras
print('Resultado do SET com elementos diferentes: ',resultado)

#7.clear() - limpar
#Remove todos elementos do set
#O Set continua existindo, mas está vazio
frutas = {'maça','banana','laranja'}
frutas.clear()
print('SET vazio: ',frutas)

#8. issubset() - verifica se é subconjunto
#Verifica se todos elementos de um set estão dentro de outro.
frutas = {'maçã','banana','laranja'}
favoritas = {'maçã','banana'}

print('Exemplo com todos elementos na lista principal: ', favoritas.issubset(frutas))