"""
Funções podem usar parâmetros para receber valores. Parâmetro é o nome da "variável" 
dentro dos parênteses,argumento é o valor passado para o parâmetro no momento da execução 
da função.

Sabendo disso, o código a seguir exibe o que na tela?
A)  16 é multiplo de 7? False
    15 é múltiplo de 3? False
    10 é múltiplo de 2? False

B) 8 é multiplo de 16? True
   3 é múltiplo de 15? True
   2 é múltiplo de 10? True

C)  16 é multiplo de 8? True
    15 é múltiplo de 3? True
    10 é múltiplo de 2? True
"""
def multiplo_de(numero, multiplo):
    resultado = numero % multiplo == 0
    print(f'{numero} é múltiplo de {multiplo}?', end=' ')
    print(resultado)

multiplo_de(16, 8)
multiplo_de(15, 3)
multiplo_de(10, 2)