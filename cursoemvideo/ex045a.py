from random import randint
from time import sleep
print('{:=^40}'.format('\033[35mJOKENPÔ\033[m'))
print('''ESCOLHA UMA OPÇÃO
[1] PEDRA
[2] PAPEL
[3] TESOURA''')
opcao = int(input('Digite a opção: '))
comp = randint(1, 3)
print('\033[32mJOO')
sleep(1)
print('KEEN')
sleep(1)
print('PÔ\033[m')
if opcao == 1 and comp == 3:
    print(f'Você venceu VC= {opcao} x Ele= {comp}')
elif opcao == 2 and comp == 1:
    print(f'Você venceu VC= {opcao} x Ele= {comp}')
elif opcao == 3 and comp == 2:
    print(f'Você venceu VC= {opcao} x Ele= {comp}')
elif opcao == comp:
    print(f'O jogo deu empate tente novamente, Vc= {opcao} x ELE= {comp}')
elif opcao >= 4:
    print('\033[31mEssa opção não existe jogue novamente!\033[m')
else:
    print(f'O computador venceu ELE= {comp} x VC= {opcao}')
