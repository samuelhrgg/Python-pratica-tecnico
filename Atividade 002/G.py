"""
G#) Você está desenvolvendo um programa para determinar 
se três segmentos podem formar um triângulo. Para isso, o programa 
precisa receber as medidas dos três segmentos e compará-las entre si.
A resposta resultante dessa comparação deve 
indicar se os segmentos fornecidos podem formar um triângulo ou não..

Curso: Técnico em Desenvolvimento de Sistemas - Senac Minas
Aluno: Samuel Gurgel
Docente: Samuel Gurgel
Data: 13/05/2026

a + b > c
a + c > b
b + c > a

"""
print()
print('Conferindo um triângulo')
ladoA = float(input('Informe o primeiro segmento em cm: '))
ladoB = float(input('Informe o segundo segmento em cm: '))
ladoC = float(input('Informe o terceiro segmento em cm: '))

if (ladoA <= 0 or ladoB <= 0 or ladoC <= 0):
    print('Os segmentos devem ser maior que 0!')

elif ((ladoA + ladoB) > ladoC) and ((ladoA + ladoC) > ladoB) and ((ladoB + ladoC) > ladoA):
    print('Os segmentos podem formar um triângulo!')

else:
    print('Os lados não podem formar um triângulo!')

print()
