'''
exemplo função intersection ('&') no set
'''

set1 = {'kwid' , 'corsa' , 'mustang'}
set2 = {'corsa' , 'mustang' , 'cherryQQ'}

e_carro = set1.intersection(set2)

print(set1)
print(set2)
print(e_carro)

lista1 = {1 , 2 , 3}
lista2 = {2 , 3 , 4}

inter = lista1 & lista2

print(lista1 , '|' , lista2)
print(inter)