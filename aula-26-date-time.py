#aula-26-date-time.py
"""
Datetime

A biblioteca datetime do Python é uma parte da biblioteca 
padrão do Python que oferece classes e funções para trabalhar
com datas e horários de forma eficiente. 

Ela permite aos desenvolvedores criar, manipular e formatar datas
e horários de acordo com as necessidades de seus programas. 

Algumas classes da datetime():

datetime: Esta classe representa uma combinação de data e horário, 
incluindo informações sobre ano, mês, dia, hora, minuto, segundo e microssegundo.

date: Esta classe representa apenas a parte da data (ano, mês e dia), 
sem qualquer informação de hora.

time: Representa apenas a parte do horário
(hora, minuto, segundo e microssegundo), sem qualquer informação de data.

"""
#Importando as bibliotecas
import os #sistema operacional
from datetime import datetime
from datetime import date #importando somente a classe date da biblioteca datetime



#Limpando o terminal
os.system('cls')

#Declaração de variavel para data
data = datetime.now() #now = agora

dataFormat = data.strftime('%d-%m-%Y')

print(f'Data sem formatação {data}')
print(f'Data formatada {dataFormat}')

#recebendo o ano
dataAtual = date.today()
nascimento = 1999
idade = dataAtual.year - nascimento
print(f'A idade é: {idade}')

data = date(2026,5,18)
dataAno = date(2026,5,18).year
dataHoje = date.today()

print(data)
print(dataAno)
print(f'Hoje é dia {dataHoje.day} e mês {dataHoje.month}')

print('-'*70)
dataQualquer = input('Informe um data qualquer: (dd/mm/aaaa): ')

dataConv = datetime.strptime(dataQualquer , '%d/%m/%Y')

print(dataConv)
print(dataConv.year)
calculo = (date.today().year - dataConv.year)
print(calculo)