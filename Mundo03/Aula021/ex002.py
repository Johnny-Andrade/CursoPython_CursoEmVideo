def parImpar(n):
    if n % 2 == 0:
        return True
    else:
        return False
    
    
num = int(input('Digite um número: '))
if parImpar(num):
    print('É par!')
else:
    print('Não é par!')
