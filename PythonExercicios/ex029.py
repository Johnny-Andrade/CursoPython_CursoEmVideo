velocidade = int(input('Qual foi a velocidade do carro em km/h? '))
multa = (velocidade - 80)*7

if velocidade > 80:
    print('Você foi multado! Precisará pagar R${}.00'.format(multa))
print('Dirija sempre com segurança!')
