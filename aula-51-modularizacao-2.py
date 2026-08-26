#aula-51-modularizacao-2.py

import modulos_py.arquivo
from modulos_py import arquivo
#from modulos_py.arquivo import variavel
from modulos_py.arquivo import *
from modulos_py.arquivo import xico

import sys
sys.path.append('c:/Users/Samuel Gurgel/Desktop')
import testando_2
from testando_2 import texto,finalizar

print(arquivo.variavel)
print(variavel)
print(xico)
print(fabio)

print(arquivo.par(7))

print('-'*70)
#print(*sys.path, sep = '\n')

print(testando_2.texto)
print(texto)
print(testando_2.finalizar())
print(finalizar())
