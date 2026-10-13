try: #Tente fazer algo
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError): #Caso dê erro (não precisa especificar, pode só deixar except)
    print(f'Erro! Os tipos de dados digitados estão incorretos.')
except ZeroDivisionError:
    print('Não é possível dividir um número por zero!')
except KeyboardInterrupt:
    print('\nO usuário preferiu não informar os dados!')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}')
else: #Caso dê certo (Opcional)
    print(f'O resultado de {a}/{b} é {r:.2f}.')
finally: #Acontece independente de erro/sucesso (Opcional)
    print('Obrigado por usar nosso programa. Volte sempre!')
