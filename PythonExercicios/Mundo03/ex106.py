from time import sleep
cores = ('\033[m', # 0 - Sem cor
         '\033[0;31m', # 1 - vermelho
         '\033[0;32m', # 2 - verde
         '\033[0;33m', # 3 - amarelo
         '\033[0;34m', # 4 - azul
         '\033[0;35m', # 5 - roxo
         '\033[7;37m', # 6 - branco
         )
def ajuda(comando):
    título(f"Acessando o manual do comando \'{comando}\'", 1)
    print(cores[6], end='')
    help(comando)
    print(cores[0], end='')
    sleep(2)
    
    
def título(msg, cor=0):
    tam = len(msg)+4
    print(cores[cor], end='')
    print('~'*tam)
    print(f'  {msg}')
    print('~'*tam)
    print(cores[0], end='')
    sleep(1)
   
    
# Programa Principal
comando = ''
while True:
    título('SISTEMA DE AJUDA PyHELP',4)
    comando = str(input("Função ou Biblioteca > "))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
título('ATÉ LOGO!',5)
