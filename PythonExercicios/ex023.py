num = int(input('Digite um número de 0 a 9999: '))
unida = num // 1 % 10
dezen = num // 10 % 10
cente = num // 100 % 10
milha = num // 1000 % 10

print("""
Unidade: {}
Dezena: {}
Centena: {}
Milhar: {}
      """.format(unida, dezen, cente, milha))
