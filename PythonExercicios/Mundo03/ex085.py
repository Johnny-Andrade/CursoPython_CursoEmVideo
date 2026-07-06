numeros = [[], []]
for c in range (1,8):
    num = int(input(f'Digite o {c}° número: '))
    if num % 2 == 0:
        numeros[0].append(num)
    else:
        numeros[1].append(num)
numeros[0].sort()
numeros[1].sort()
print(f'Os números pares em ordem crescentes, são: {numeros[0]}')
print(f'Os números ímpares em ordem crescente são: {numeros[1]}')
print(f'\nPor fim, a lista completa é: {numeros}')
