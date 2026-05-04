ini = int(input('Digite o início da contagem: '))
fim = int(input('Digite onde termina a contagem: '))
pas = int(input('Digite o passo: '))
if pas == 0:
    print('Passo inválido, tornando passo 1.')
    if ini < fim:
        pas = 1
    elif ini > fim:
        pas = -1
if (ini > fim and pas > 0) or (ini < fim and pas < 0):
    print('\033[33mInvertendo passo...\033[m')
    pas = pas * (-1)
if ini > fim:
    for c in range(ini, fim-1, pas):
        print(c)
else:
    for c in range(ini, fim+1, pas):
        print(c)
