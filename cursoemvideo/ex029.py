from time import sleep
import emoji
velocidade = float(input('Velocidade registrada... '))
print('Processando caluculo...')
sleep(2)
if velocidade > 80:
    multa = (velocidade - 80)*7
    print('Você foi multado em R${}'.format(multa))
else:
    print('Velocidede permitida! Diriga com segurança.')
print(emoji.emojize(':alien:'*20, use_aliases=True))
