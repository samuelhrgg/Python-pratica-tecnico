"""
A#.Faça um programa que leia um número indeterminado de notas (pressione ‘s’ ou ‘0’ para sair).
Após esta entrada de dados, faça o seguinte:
 • Mostre a quantidade de notas que foram lidas.
 • Exiba todas as notas na ordem em que foram informadas.
 • Exiba todas as notas na ordem inversa à que foram informadas, uma abaixo da outra.
 • Calcule e mostre a soma das notas.
 • Calcule e mostre a média das notas.

 
 Autor: Samuel Gurgel
 Data: 16/06/2026

"""
notas = []

while True:
    nota = input('Digite uma nota(0 ou S para sair:')
    
    if nota == '0' or nota == 's' or nota == 'S':
        break
    try:
        notasConvertida = float(nota)
        notas.append(notasConvertida)
    except:
        print('Informe um valor ou "s" para sair')

print(f'Quantidade de notas: {len(notas)}')

soma = 0

#realizar a soma
for x in notas:
    soma += x

#media
media = soma/len(notas)

print(f'Soma das notas: {soma}')
print(f'Média das notas: {media}')
print(f'Notas na ordem informada: {notas}')
print(f'Notas na ordem inversa: ')
notas.reverse()
for x in notas:
    print(f'{x}')
