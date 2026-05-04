print('Entre 1 e 500, a soma dos múltiplos de três ímpares é: ')
s = 0
for c in range(1, 501):
    if c % 3 == 0:
        if c%2 != 0:
            s += c
print(s)
