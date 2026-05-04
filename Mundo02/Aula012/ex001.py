nome = str(input('Qual seu nome? ')).strip().title()
if nome == 'Johnny':
    print('Um belo nome!')
elif nome == 'Camilla':
    print('Eu amo alguém com esse nome!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Que nome comum...')
else:
    print('Definitivamente um dos nomes...')
print('Tenha um bom dia, {}!'.format(nome))
