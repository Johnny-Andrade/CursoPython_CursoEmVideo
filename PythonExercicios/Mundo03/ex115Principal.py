from ex115 import menu
from time import sleep
while True:
    resposta = menu.interface(['Ver pessoas cadastradas','Cadastrar nova pessoa','Sair do Sistema'])
    if resposta == 1:
        menu.cabeçalho('opção 1')
    elif resposta == 2:
        menu.cabeçalho('opção 2')
    elif resposta == 3:
        menu.cabeçalho('Saindo do programa...')
        break
print('Volte sempre!')
