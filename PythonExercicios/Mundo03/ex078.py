valores = []
for n in range(0,5):
    valores.append(int(input(f'Digite um número para a posição {n}: ')))
maior = max(valores)
menor = min(valores)
print('-='*10)
print(f'Você digitou os valores {valores}')
print(f'O maior valor é {maior}, que está nas posições ', end='')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}, ',end='')
print('e só!')
print(f'O menor valor é {menor}, que está nas posições ', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}, ',end='')
print('e só!')
