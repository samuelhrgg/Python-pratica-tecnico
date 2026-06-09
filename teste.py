
import os

os.system('cls')

print('-' * 50)
print('VERIFICADOR DE PALÍNDROMO')
print('-' * 50)

fraseOriginal = input('Informe um frase: ')
tamanhoFrase = len(fraseOriginal)
frase1 = (fraseOriginal.lower()
          .replace(' ', '')
          .replace('á', 'a')
          .replace('à', 'a')
          .replace('ã', 'a')
          .replace('â', 'a')
          .replace('é', 'e')
          .replace('ê', 'e')
          .replace('í', 'i')
          .replace('ó', 'o')
          .replace('ô', 'o')
          .replace('õ', 'o')
          .replace('ú', 'u')
          .replace('ç', 'c')
          .replace(',','')
          .replace('-','')
          .replace('!',''))
frase2 = frase1[::-1]
print(frase1)
print(frase2)

print()
if frase1 == frase2:
    print('É um palíndromo')
    
else:
    print('Não é um palíndromo')

print()
print(f'Frase original: {fraseOriginal}')
print(f'Frase em palíndromo: {frase2}')    

print()
