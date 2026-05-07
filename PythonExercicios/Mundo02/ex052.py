print('-='*20)
print('Identificador de N° Primo')
print('-='*20)
num = int(input('Diga um número inteiro: '))
tot = 0
for c in range(1, num+1):
    if num % c == 0:
        tot += 1  
print('\n\033[mO número {} foi divisível {} vezes.'.format(num, tot))
if tot == 2:
    print('Logo, ele \033[32mÉ PRIMO\033[m')
else:
    print('Portanto, ele \033[31mNÃO É PRIMO\033[m')
