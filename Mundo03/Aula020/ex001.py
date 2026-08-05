def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma {a} + {b} = {s}')
    print()


#Programa Princiapl
soma(4, 5)
soma(8, 9)
soma(2, 1)
soma(b=3, a=7) #Se for explicitar, precisa fazer com os dois: soma(b=3, 7) não funciona!
