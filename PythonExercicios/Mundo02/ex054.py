from datetime import date
maiori = 0
menori = 0
anoatual = date.today().year
for pessoa in range(1,8):
    nasci = int(input('Em que ano a {}° pessoa nasceu? '.format(pessoa)))
    if (anoatual - nasci) >= 21:
        maiori += 1
    else:
        menori += 1
print('Ao todo, tivemos: \n{} pessoas na maioridade.\n{} pessoas na menoridade.'.format(maiori, menori))
