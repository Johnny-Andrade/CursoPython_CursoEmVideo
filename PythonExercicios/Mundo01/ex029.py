velocidade = float(input('Qual foi a velocidade do carro em km/h? '))

if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('Você foi multado por exceder 80km/h! Precisará pagar R${:.2f}'.format(multa))
print('Dirija sempre com segurança!')
