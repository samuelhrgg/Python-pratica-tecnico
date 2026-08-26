#arquivo.py

__all__ = [
    'fabio',
    'variavel'
]

variavel = 'Teste'
fabio = 'Fábio'
xico = 'Xico'

def par(x):
    if x % 2 == 0:
        return 'Par'
    else:
        return 'Impar'