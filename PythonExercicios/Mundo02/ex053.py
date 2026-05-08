print('-='*20)
print('Identificador de Palindromos')
print('-='*20)
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
palavjunto = ''.join(palavras)
inverso = ''
'''for letra in range(len(palavjunto)-1, -1, -1): 
    #número de letras -1 (pq começa no 0), vai até a letra 0 (-1 pq é do for) voltando de 1 em 1 letra
    inverso += palavjunto[letra]'''
inverso = palavjunto[::-1] 
print('Você digitou: \n{} \nInvertendo, temos:\n{}'.format(palavjunto, inverso))
if inverso == palavjunto:
    print('\033[32mTemos um palíndromo\033[m!')
else:
    print('Mas isso \033[31mnão é palíndromo\033[m...')
