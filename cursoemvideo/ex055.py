maior = 0
menor = 0
for c in range(1, 6):
    peso = int(input('Digite o peso da {} pessoa: '.format(c)))
    if c == 1: #primeiro laaço para atribuir o peso para ambas as variaveis!!! LEGAL
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso digitado é {}'.format(maior))
print('O menor peso digitado é {}'.format(menor))
