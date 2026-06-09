tupla = (int(input('Digite um número: ')), 
         int(input('Digite um número: ')), 
         int(input('Digite um número: ')), 
         int(input('Digite um número: ')))
pares = 0
print(f'O número 9 apareceu {tupla.count(9)} vezes' if 9 in tupla 
      else 'Não há número 9.')
print(f'O número 3 apareceu primeiro na {tupla.index(3)+1}° posição.' if 3 in tupla 
      else 'Não há número 3.')
for num in tupla:
    if num % 2 == 0:
        pares += 1
if pares > 0:
    print(f'A quantidade de números pares é {pares}. Sendo: ', end='')
    for n in tupla:
        if n % 2 == 0:
            print(f'{n} ', end='')
else:
    print('Não há números pares.')
