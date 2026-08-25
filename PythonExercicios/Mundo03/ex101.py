from datetime import datetime
AnoAtual = datetime.now().year
def voto(ano = AnoAtual):
    idade = AnoAtual - ano
    if idade >= 18 and idade < 65:
        return print(f'Com {idade} anos: VOTO OBRIGATÓRIO.')
    elif idade >= 16 or idade >= 65:
        return print(f'Com {idade} anos: VOTO OPCIONAL.')
    else:
        return print(f'Com {idade} anos: NÃO VOTA.')


print('--'*20)
nascimento = int(input('Em que ano você nasceu? '))
voto(nascimento)
