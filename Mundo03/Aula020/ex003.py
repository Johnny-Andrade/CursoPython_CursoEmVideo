def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1
    print(f'O novo valor é:\n {lst}')


lista = [7, 2, 5, 0, 4]
print(lista)
dobra(lista)
