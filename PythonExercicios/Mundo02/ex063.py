print('-='*20)
print('Fibonaccizando..')
print('-='*20)
fiboN = int(input('Escreva quantos números na sequencia de Fibonacci você quer: '))
contador = 1
anterior = 1
atual = 1
if fiboN == 0:
    print('[ERRO] Tente novamente')
elif fiboN == 1:
    print('0 > ', end='')
else:
    print('0 > ', end='')
'''     while contador < fiboN:
        print(atual, end=' > ')
        atual += anterior
        anterior = atual 
        contador +=1
        '''       
print('FIM')