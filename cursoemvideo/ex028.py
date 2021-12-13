import random
import time
print('-=-'*20)
n = int(input('Qual o numero que o computador vai escolher de 0 a 5? '))
print('-=-'*20)
print('PROCESSANDO...')
time.sleep(3)
rad = random.randint(0,5)
if rad == n:
    print('Acertou Miseravi!VENCEU!')
else:
    print('O computador venceu!PEEERDEUUU!')
print('-=-'*20)
print('O computador pensou no numero {}'.format(rad))
print('-=-'*20)
