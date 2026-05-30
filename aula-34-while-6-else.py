#aula-34-while-6-else.py

#While/else específico de python

string = 'Valor qualquer'
i = 0

while i < len(string):
    letra = string[i]
    # if letra == ' ':
    #     break
    print(letra)
    i += 1
    break

#o Else em while só é exibido com o while é completado sem interrupções
else:
    print('O else foi executado')
    #print('Não econtrei espaço na String')

print('Fora do While')