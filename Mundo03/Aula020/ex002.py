def contador(*num): #Assim, indicamos que é uma quantia qualquer de valores, e cria-se uma tupla
    for item in num:
        print(item, end=' ')
    print(f'\nNessa tupla, temos {len(num)} valores!')


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)
