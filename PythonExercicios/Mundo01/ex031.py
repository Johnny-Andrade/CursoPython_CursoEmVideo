viagem = float(input('Digite a distância da viagem em KM: '))
# if viagem <=200:
#     preco = viagem/2
# else:
#     preco = viagem*0.45
preco = viagem * 0.5 if viagem <= 200 else viagem * 0.45
print('O preço da viagem será R${:.2f}'.format(preco))
print('Obrigado pela preferência!')
