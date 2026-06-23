galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galera[0][0])
print(galera[2][1])
for nomes in galera:
    print(nomes[0])
for idades in galera:
    print(idades[1])
print('-='*20)
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade')
    