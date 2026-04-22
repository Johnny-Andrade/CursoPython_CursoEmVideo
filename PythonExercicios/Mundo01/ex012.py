preco = float(input('Digite o preço de seu produto: R$'))

print('Parabéns! Por digitar corretamente, você receberá desconto de 5%!')
print('Você ia pagar R${:.2f}, mas agora vai pagar apenas R${:.2f} !'.format(preco, preco*0.95))
