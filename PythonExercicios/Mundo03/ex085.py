pares = list()
impares = list()
numeros = [pares, impares]
for n in range (1,8):
    num = int(input(f'Digite o {n}° número: '))
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
pares.sort()
impares.sort()
print(f'Os números pares em ordem crescentes, são: {numeros[0]}')
print(f'Os números ímpares em ordem crescente são: {numeros[1]}')
print(f'Por fim, a lista completa é: {numeros}')
