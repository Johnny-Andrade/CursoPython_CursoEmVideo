import urllib
import urllib.request as urlreq

try:
    site = urlreq.urlopen('https://google.com.br/')
except: #o Erro é urllib.error.URLError
    print('\033[31m[ERRO]\033[m O Site está fora do ar ou inacessível pelo seu computador.')
else:
    print('Tudo OK! O site pode ser acessado normalmente.')
    #print(site.read())    
