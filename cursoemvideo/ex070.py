eslogam = 'LOGA DE PRODUTOS'
print('-=-'*15)
print('{:^40}'.format(eslogam))
print('-=-'*15)

menorPRECO = ' '
menor = total = cont = contMIL = 0
while True:
    nome = str(input('Qual é o nome do produto: ')).strip().upper()
    preco = float(input('Qual é o preço do produto: '))
    if cont == 0:
        menor = preco
    if preco <= menor:
        menorPRECO = nome
    if preco > 1000:
        contMIL += 1
    total += preco
    cont += 1
    while True:
        resp = str(input('Dedeja continuar? [S/N] ')).strip().upper()
        if resp == 'S' or resp == 'N':
            break
    if resp == 'N':
        break

print('O total gasto na compra é {}'.format(total))
print('{} produtos custam mais que R$1000,00'.format(contMIL))
print('o produto com o menor preço é {}'.format(menorPRECO))
