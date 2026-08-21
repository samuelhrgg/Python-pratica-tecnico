#aula-50-modularizacao.py

#Modularização - Entendendo os seus próprios módulos Python
#O primeiro modulo executado chama-se __main__
#Você pode importar outro módulo inteiro ou parte do módulo
#O python conhece a pasta onde o 'main' está e as pastas abaixo dele
#Ele não reconhece pastas e módulos acima do 'main' por padrão
#O python conhece todos os módulos e pacotes presentes nos 
# caminhos de sys.path

import aula_50_modulo_teste
from aula_50_modulo_teste import samuel,pedro,linha

#print('Este módulo se chama ' , __name__)
print(aula_50_modulo_teste)
print(aula_50_modulo_teste.pedro , aula_50_modulo_teste.samuel)
print(samuel,pedro)

#Usando somente o import aula_50_modulo_teste
print(aula_50_modulo_teste.linha(70))

#Usando o from aula_50_modulo_teste import linha
print(linha(70))
