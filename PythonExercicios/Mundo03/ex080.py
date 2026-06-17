lista = []
for n in range(0,5):
    valor = int(input('Digite um valor: '))
    if n == 0:
        lista.append(valor)
        menor = maior = valor
        print('Adicionado no final da lista...')
    elif n == 1:
        if valor < menor:
            lista.insert(0, valor)
            menor = valor
            print('Adicionado na posição 0 da lista...')
        else:
            lista.append(valor)
            print(f'Adicionado na posição 1 da lista...')
            maior = valor
    elif valor > maior:
        lista.insert((lista.index(maior)+1), valor)
        maior = valor
        print('Adicionado no final da lista...')
    elif valor < menor:
        lista.insert((lista.index(menor)),valor)
        print(f'Adicionado na posição {lista.index(menor)} da lista...')
        menor = valor
    elif valor in lista:
        lista.insert(lista.index(valor), valor)
        print(f'Adicionado na posição {lista.index(valor)} da lista...')
    elif valor > menor and valor < maior:
        for num in lista:
            if lista.index(num) == 0 or lista.index(num) == 1:
                if valor < num:
                    meioG = num
                if valor > num:
                    meioP = num
            elif meioP > num and valor < num:
                meioP = num
            elif meioG < num and valor > num:
                meioG = num
        diferença = (lista.index(meioG) - lista.index(meioP))
        lista.insert(diferença, valor)
        print(f'Adicionado na posição {diferença} da lista...')
print(f'Os valores digitados, ordenados, são: {lista}')
