#condições
nome = str(input('Digite seu nome: ')).strip().lower()
if 'isis' in nome:
    print('Que nome bonito vc tem!')
else:
    print('Você ainda pode mudar seu nome!')
print('fim')

#media
n1 = float(input('Digite sua nota: '))
n2 = float(input('Digite outra nota: '))
media = (n1 + n2)/2
if media >= 7:
    print('PARABÉNS aprovado!')
else:
    print('Ficou de exame!')
