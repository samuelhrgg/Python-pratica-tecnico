#aula-49-try-except-2.py
#Erros não devem passar silenciosamente

try:
    a = 18
    b = 0
    c = 'Samuel'
    print('Teste')
    #print(c[9])
    print(samuel)

except ZeroDivisionError:
    print('Você tentou dividir por zero.')

except NameError:
    print('Uma variável não foi definida')

except (TypeError,IndexError) as error: #capturar o erro
    print('Type Error + IndexError')
    print('MSG: ' , error)
    print('MSG: ', error.__class__.__name__) #trás formatado o erro

except Exception: #representa 'todos os erros', a maior classe dos erros
    print('Erro desconhecido')
