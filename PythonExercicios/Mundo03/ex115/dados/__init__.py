from ex115.menu import *
def arquivoExiste(nome):
    try:
        a = open(nome, 'rt') #rt = read text, ler um arquivo de texto
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+') #wt = write text, escrever um arquivo de texto, o + é pra criar
        a.close()
    except:
        print('\033[31mHouve um erro na criação do arquivo!\033[m')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('\033[31mErro ao ler o arquivo!\033[m')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        print(a.read())

