from random import randint

cont = 0
tab = '\033[32mVAMOS JOGAR PAR OU IMPAR\033[m'
while True:
    print('-=-'*10)
    print('{}'.format(tab))
    print('-=-'*10)
    comp = randint(0, 10)
    jogar = str(input('Par ou Impar? Digite [P/I] para jogar! ')).upper().strip()
    jogador = int(input('Digite um numero de 0 até 10: '))
    res = (comp + jogador) % 2
    if jogar == 'P' and res == 0:
        print('Você venceu o computador jogou {}'.format(comp))
        cont += 1
        print('o resulatado foi {}'.format(comp + jogador))
    elif jogar == 'I' and res != 0:
        print('Você venceu o computador jogou {}'.format(comp))
        cont += 1
        print('o resulatado foi {}'.format(comp + jogador))
    else:
        print('Você perdeu o computador jogou {}'.format(comp))
        print('o resulatado foi {}'.format(comp + jogador))
        break

print('obrigado por jogar, você venceu um total de {} vezes'.format(cont))
print('\033[31mfim\033[m')
