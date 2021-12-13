import emoji
import random
from time import sleep
print('\033[32mJOGO PAPEL PEDRA TESOURA\033[m')
jogador = (str(input('Desafie o computador é a sua vez! '))).strip().lower()
print('\033[31mÉ a vez do computador...se empatar ele também ganha...\033[m')
sleep(3)
tesoura = emoji.emojize(':v:', use_aliases=True)
pedra = emoji.emojize(':punch:', use_aliases=True)
papel = emoji.emojize(':hand:', use_aliases=True)
comp = [tesoura, papel, pedra]
comp = random.choice(comp)
if jogador == 'tesoura' and comp == papel:
    print(tesoura, ' x ', comp, 'Você venceu, \033[31mPARABÉNS')
elif jogador == 'pedra' and comp == tesoura:
    print(pedra, 'x ', comp, 'Você venceu, \033[31mPARABÉNS')
elif jogador == 'papel' and comp == pedra:
    print(papel,' x ', comp, 'Você venceu, \033[31mPARABÉNS')
else:
    print('Você perdeu tente de novo! O computador jogou', comp)
