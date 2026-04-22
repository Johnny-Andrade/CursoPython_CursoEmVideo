dias = float(input('O carro foi alugado por quantos dias? '))
kilo = float(input('Quantos Kms foram rodados? '))
aluguel = (dias*60)+(kilo*0.15)
print('A diária é R$60,00 mais R$0,15 por Km.\nLogo, você deve pagar R${:.2f}'.format(aluguel))
