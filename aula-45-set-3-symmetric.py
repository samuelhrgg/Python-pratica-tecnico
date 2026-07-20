"""
Método Set Symmetric

É usado para retornar um novo conjunto contendo todos os elementos
que estão presentes em qualquer um dos conjuntos mas não em ambos
"""

#Exemplo 1

ALbum_Davi = {'Cr7' , 'Neymar' , 'Messi' , 'Lamine Yamal'}

Album_xico = {'Cr7' , 'Neymar' , '67' , 'Messi'}

dif = ALbum_Davi.symmetric_difference(Album_xico)

print(dif)

#Também funciona para comparar um set a uma list ou tupla

album = list(Album_xico)

x=ALbum_Davi.symmetric_difference(album)

print(x)