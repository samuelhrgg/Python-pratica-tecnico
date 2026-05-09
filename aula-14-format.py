#Função format com python!

A = 1
B = 2
C = 3

texto1 = 'a→{} b→{} c→{}'.format(A,B,C) #direto
texto2 = 'a→{0} b→{0} c→{2}'.format(A,B,C) #com indice
texto3 = 'a→{nome1} b→{nome2} c→{nome3}'.format(nome1=A,nome2=B,nome3=C) #nomeado

print(texto1)
print(texto2)
print(texto3)

#praticando format ↓
nome = 'Samuel'
idade = '26'

#Fazendo direto por ordem de variável
texto4 = 'Nome {} e Idade {}'.format(nome,idade)
print(texto4)
#Utilizando indice das variáveis
texto5 = 'Nome {0} e Idade {1}'.format(nome,idade)
print(texto5)
#Utilizando nomeação das variáveis
texto6 = 'Nome {name} e Idade {age}'.format(name=nome , age=idade)
print(texto6)
