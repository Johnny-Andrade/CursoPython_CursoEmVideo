tupla = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 
         'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99, 
         'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
print('-='*15)
print('{: ^30}'.format('LISTAGEM DE PREÇOS'))
print('-='*15)
for item in tupla:
    if tupla.index(item) % 2 == 0:
        print(f'{item:.<20}',end='')
    else:
        print(f'R$ {item:>6.2f}')
