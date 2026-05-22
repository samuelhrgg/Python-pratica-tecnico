#aula-30-fatiamento-strings.py

"""
Fatiamento de Strings

 012345678
 Olá mundo
-987654321

Fatiamento[i:f:p] → (i) início | (f) fim | (p) 'passos'

"""
variavel = 'Olá mundo'
print(variavel[4]) #pegar letra m

#fatiamento [i:f:] começando do ínicio ''i''
print(variavel[4:]) #escrever do índice 4 até o final 'mundo'
print(variavel[0:3]) #ir da letra 'o' até 'á' - olá
print(variavel[:3]) #também pode omitir o ínicio

print(variavel[0:9:1]) #exibir variável inteira
print(variavel[0:9:2]) #exibir de 2 em 2 letras
print(variavel[::-1]) #exibir invertido
print(variavel[-1:-10:-1]) #exibir invertido
print(variavel[-1:-10:-3]) #exibir invertido

num = 1234
print(str(num)[::-1])