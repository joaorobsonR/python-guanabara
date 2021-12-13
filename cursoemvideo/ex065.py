soma = maior = menor = cont = 0
confe = str(input('Digite S para continuar ou N para parar ')).upper().strip()
while confe == 'S':
    n = int(input('digite um numero: '))
    cont += 1
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    soma += n
    confe = str(input('Digite S para continuar ou N para parar ')).upper().strip()
media = soma/cont
print('o maior valor é {}, menor é {}, a media {}'.format(maior, menor, media))
