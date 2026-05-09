#Formatação de strings utilizando f-strings no python

nome = 'Samuel Gurgel'
altura = 1.76
peso = 80
IMC = peso / (altura ** 2) #Declaração de constantes

#método tradicional
print(nome, 'tem', altura, 'de altura')
#utilizando f-strings
print(f'{nome} tem {altura} de altura')

#método tradicional
print('Pesa', peso , 'quilos e seu IMC é', IMC)
#utilizando f-strings
resposta=(f'Pesa {peso} quilos e seu IMC é {IMC:.1f}')

print(resposta)