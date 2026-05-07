print('Os números pares entre 1 e 50 são: ')
for c in range(2, 51, 2):
    print('\033[32m{}\033[m, '.format(c),end = '')
print('Fim!')
