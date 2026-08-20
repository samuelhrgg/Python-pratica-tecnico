#aula-47-isinstance.py

#isinstance - Para saber se o objeto é de determinado tipo

a = 10
b = isinstance(a,str)
print(b)
print(isinstance(a,int))

lista = [
    'a' , 1 , 1.1, True, [0,1,3] , (1,2),
    {0,1} , {'nome' : 'Luiz'}
]

print('-' * 50)
for item in lista:
    if isinstance(item,set):
        print('SET')
        item.add(5)
        print(item , isinstance(item,set))

    elif isinstance(item,str):
        print('STR')
        print(item.upper())

    elif isinstance(item,(int,float)):
        print('Numeros')
        print(item , item * 2)

    else:
        print('Outro')

