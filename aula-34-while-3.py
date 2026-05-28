#aula-34-while-3.py

#While (continue)

contar = 0
while (contar <= 100):

    contar += 1
    
    if contar == 6:
        #print('Não vou mostrar o 6')
        continue #ignora o restante

    if contar >= 10 and contar <= 27:
        #print(f'Não vou exibir o {contar}')
        continue

    print(contar)

    if contar == 40:
        break #parar o laço

print('Saiu do Contar')