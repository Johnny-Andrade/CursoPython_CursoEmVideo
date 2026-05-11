r = 'S'
while r == 'S': #while é melhor usado quando não se sabe quantas repetições são.
    n = int(input('Digite um número: '))
    r = str(input('Quer continuar? [S/N]: ')).strip().upper()
print('Fim!')
