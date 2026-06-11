num = [2, 5, 9, 1]
print(f'Começa com {num}')
num[2] = 3
num.append(7)
num.insert(2, 0) #Adicionou o 0 na posição 2
print(f'Agora é {num}')
num.sort()
print(f'Arrumando, temos {num}')
if 8 in num:
    num.remove(8) #remove() remove o item, em sua primeira aparição
else:
    print('Não há número 8 na lista.')
num.pop(4) #pop() remove o elemento na posição 4
num.sort(reverse = True)
print(f'Tirei o 5...\nPodemos sempre inverter, agora temos {num}')
print(f'Essa lista tem {len(num)} elementos!')
