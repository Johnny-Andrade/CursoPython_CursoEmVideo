preco = float(input('Digite o preço do produto, por favor: R$'))
print('--'*20)
print('Digite 1 para pagamento à vista com dinheiro ou cheque.\nDigite 2 para pagamento à vista no cartão.\nDigite 3 para pagamento em até 2x no cartão.')
fpaga = int(input('Digite 4 para pagamentos acima de 3x no cartão: '))
print('--'*20)
if fpaga == 1:
    print('Legal! Você reberá 10% de desconto, o preço vai de R${:.2f} para R${:.2f}!'.format(preco, preco*0.9))
elif fpaga ==2:
    print('Boa! Você receberá 5% de desconto, o preço de R${} se torna R${}!'.format(preco, preco*0.95))
elif fpaga == 3:
    print('Okay! Você pagará duas parcelas de R${}, totalizando R${}.'.format(preco/2,preco))
elif fpaga == 4:
    print('Certo. Com os juros, o preço total vai de R${} para R${}.'.format(preco, preco*1.2))
else:
    print('\033[31m[ERRO]\033[m Reinicie o programa, e escolha corretamente.')
