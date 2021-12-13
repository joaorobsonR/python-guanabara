d = float(input('\033[33mQual a distância da viagem? '))
d1 = d * 0.5
d2 = d * 0.45
if d <= 200:
    print('O preço da passagem é \033[31m{}\033[m'.format(d1))
else:
    print('O preço da passagem é \033[31m{}\033[m'.format(d2))
