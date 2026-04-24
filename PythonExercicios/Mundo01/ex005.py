num = int(input('Digite um número: '))
print('O número escolhido é \033[31m{}\033[m. \nSeu antecessor é \033[7;34m{}\033[m. \nSeu sucessor é \033[1;35m{}\033[m'.format(num, (num-1), (num+1)))
