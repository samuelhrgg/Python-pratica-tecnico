#aula-41-gerador-cpf-1.py
"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
  ___________________________
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""
cpf = input('Informe os 9 dígitos do CPF: ')
cpfLista = []
contagem = 10
soma = 0

for x in range(len(cpf)):
    cpfLista.append(cpf[x])

for y in cpfLista:
    multi = int(y)*contagem
    soma += multi
    contagem -= 1

resultado = soma * 10
resto = resultado % 11

if resto > 9:
    digito = 0

else:
    digito = resto

print(f'Primeiro dígito do CPF: {digito}')

novoCPF = cpfLista.copy()
novoCPF.append(digito)

contagem = 11
soma = 0

for y in novoCPF:
    multi = int(y) * contagem
    soma += multi
    contagem -= 1

resultado = soma * 10
resto = resultado % 11

if resto > 9:
    digito2 = 0
else:
    digito2 = resto

novoCPF.append(digito2)

print(f'Segundo digito do CPF: {digito2}')
print('CPF COMPLETO:')

for x in novoCPF:
    print(x , end = '')


