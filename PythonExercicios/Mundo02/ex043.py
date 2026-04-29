print('-='*20)
print('Calculadora de IMC')
print('-='*20)
peso = float(input('Insira seu peso: '))
altura = float(input('Insura sua altura em m: '))
imc = peso/(altura**2)
print('Seu IMC é {:.2f}'.format(imc))
if imc < 18.5:
    print('Você está abaixo do peso!')
elif imc <= 25:
    print('Que legal, seu peso está ideal!')
elif imc <=30:
    print('Tome cuidado, você está em sobrepeso..')
elif imc <= 40:
    print('Eita, você está com obesidade, tome cuidado!!')
else:
    print('Você está com obesidade mórbida, cuidado!')
print('Lembre-se de se alimentar e exercitar de forma saudável!')
