"""
#Desafio o que vai mostrar?
A - 'Número menor que 2' 4
B - 'Número maior que 2' 3
C - 'Número maior que 3' 2
D - 'Número menor que 3' 2
E - 'Número menor que 1'

"""
numero = 3

if numero > 1:
    if numero > 2:
        if numero > 3:
            print('Número maior que 3')
        else:
            print('Número menor que 3')
    else:
        print('Número menor que 2')
else:
    print('Número menor que 1')