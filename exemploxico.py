'''
exemplo .remove
'''

alfabeto = {'A' , 'B' , 'C' , 'D'}

print(alfabeto)

letra_usuario = int(input('digite uma letra = '))

alfabeto.add(letra_usuario)

print(alfabeto)

alfabeto.remove(letra_usuario)


print(alfabeto)