from random import randint
from time import sleep
cont = 0
joga = 0
print('''\033[31mEm quantas tentativas você acerta?
Desafie o computador!!!\033[m''')
inicia = str(input('Digite aceita [A] or não [N] ')).strip().upper()
if 'A' in inicia:
    print('O computador está jogando...')
    sleep(3)
    comp = randint(0, 10)
    while comp != joga:
        joga = int(input('Qual o numero que o computador escolheu? '))
        if comp > joga:
            print('Ainda não, um pouco mais...')
        else:
            print('Ainda não, um pouco menor...')
        cont += +1
    print('\033[33mParabéns vc acertou em {} tentativas'.format(cont))
    print('O computador jogou {}\033[m'.format(comp))
else:
    print('\033[31mFIM\033[m')
