#Precedência em python - 
#Ordem como é executado os cálculos matemáticos 

#1. (n+n) parêntesis é o primeiro a ser executado 
#2. ** exponênciação → número elevado 5² → 5**2
#3. * / // % → Multiplicação, divisão, divisão inteira e mod
#4. + - Adição e subtração 

#2 elevado à 10 = 1024

conta_1 = 1+1 ** 5+5
conta_2 = (1+1) ** (5+5)

print(conta_1)
print(conta_2)

