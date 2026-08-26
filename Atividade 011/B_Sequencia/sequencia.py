def sequencia_ate_n(x,step):
    for x in range(1,x+1,step):
        print(f'{x}' , end = ' - ')

def pares_ate_n(x,step):
    for x in range(2,x+1,step):
        if x % 2 == 0:
            print(f'{x}' , end = ' - ')

def impares_ate_n(x,step):
    for x in range(1,x+1,step):
        if x % 2 != 0:
            print(f'{x}' , end = ' - ')
