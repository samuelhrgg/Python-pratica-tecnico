"""
Método UNION

Ele é um método alem do pipe | que faz a união de dois conjuntos
Combinando elementos de um ou mais conjuntos

"""

#Ex: Tenho duas metades de uma laranja:

#Se realmente fosse possível uni-las novamente
#Eu faria da seguinte maneira

metade_1= {'laranja1'}

metade2 = {'laranja2'}

laranjacompleta = metade_1.union(metade2)

print(laranjacompleta)

laranjacompleta2 = metade2 | metade_1

print(laranjacompleta2)