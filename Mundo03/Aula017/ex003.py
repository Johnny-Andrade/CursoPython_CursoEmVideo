a = [2, 3, 4, 7]
b = a
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
print('Quando igualamos listas, elas ficam ligadas e alterações em uma mudam a outra.')
b = a[:] #Assim fazemos listas iguais sem ligá-las
b[2] = 7
print(f'Nova lista B: {b}')
