from datetime import datetime
nome = str(input('Nome: ')).strip()
anoatual = datetime.now().year
idade = anoatual - int(input('Ano de nascimento: '))
while idade < 0:
    idade = anoatual - int(input('\033[31m[ERRO]\033[m Ano de nascimento:'))
ctps = int(input('Carteira de Trabalho [0 = Não possui]: '))
dados = {'Nome': nome, 'Idade': idade, 'CTPS': ctps}
if ctps != 0:
    contratacao = int(input('Ano de Contratação: '))
    dados['Contratação'] = contratacao
    dados['Salário'] = float(input('Salário: R$'))
    dados['Aposentadoria'] = (35 - (anoatual - contratacao)) + idade
print(dados)
for key, item in dados.items():
    print(f'  - {key} tem valor {item}')
