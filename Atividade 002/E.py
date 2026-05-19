"""
E#) A empresa "TravelCalc" está desenvolvendo um sistema de cálculo de 
preços de passagens de ônibus com base na distância da viagem. Eles 
precisam de um programa que solicite ao usuário a distância a desejada
e,em seguida, calcule o preço da passagem de acordo com as políticas da empresa.
Segundo essas políticas, viagens de até 200 km têm um custo de R$0,70 por 
km rodado, enquanto viagens acima dessa distância passam a custar
R$0,40 por km rodado.

Curso: Técnico em Desenvolvimento de Sistemas - Senac Minas
Aluno: Samuel Gurgel
Docente: Samuel Gurgel
Data: 13/05/2026

"""
print()
print('-'*70)
print('Cálculo de Viagem')
distancia = float(input('Informe a distancia da viagem em km: '))

if distancia <= 0:
    print('A viagem informado é invalida!')

elif distancia <= 200: #se a distância for menor ou igual à 200
    valor = distancia * 0.70

else:
    valor = distancia * 0.40

print(f'O valor da passagem: R${valor:.2f}')
print('-'*70)
print()