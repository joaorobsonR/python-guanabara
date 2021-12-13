from time import sleep
import emoji
ordem = str(input('Esperando ordem OK ou NOT ')).strip().upper()
if ordem == 'OK':
    print('\033[32mATENÇÃO PARA CONTAGEM!!!\033[m')
    for c in range(10, -1, -1):
        print(c)
        sleep(1)
    print(emoji.emojize(':boom:'':boom:'':boom:'':boom:'':rocket:', use_aliases=True))
else:
    print('\033[31mABORTADO\033[m')
