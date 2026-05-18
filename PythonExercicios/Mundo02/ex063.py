print('-='*20)
print('Fibonaccizando..')
print('-='*20)
fiboN = int(input('Escreva quantos números na sequencia de Fibonacci você quer: '))
t1= 0
t2 = 1
if fiboN == 0:
    print('\033[31m[ERRO]\033[m Tente novamente.')
elif fiboN == 1:
    print('0 > Fim!')
else:
    print('{} > {}'.format(t1, t2), end='')
    cont = 3
    while cont <= fiboN:
        t3 = t1 + t2
        print(' > {}'.format(t3),end='')
        cont +=1
        t1 = t2
        t2 = t3
    print(' > Fim!')
print('~~'*20)
