galera = list()
dado = list()
maiori = menori = 0
for c in range (0,5):
    dado.append(str(input('Nome: ')).strip())
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
print(galera)
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade!')
        maiori += 1
    else:
        print(f'{p[0]} é menor de idade!')
        menori += 1
print(f'Temos um total de {maiori} adultos e {menori} crianças/adolescentes.')
