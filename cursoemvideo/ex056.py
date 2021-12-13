media = 0
velho = 0
nvelho = ''
cont = 0
contm = 0
for c in range(1, 5):
    print('=-=-=-=-={}°pessoa=-=-=-=-='.format(c))
    nome = str(input('Digite seu nome: ')).strip().upper()
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Digite o sexo [M/F] ')).strip().upper()
    media = idade + media
    if sexo == 'M':
        if idade > velho:
            velho = idade
            nvelho = nome
            contm += 1
    if sexo == 'F' and idade < 20:
        cont += 1
print('A media da idade do grupo é {} anos'.format(media/4))
if contm == 0:
    print('Não há homens nesse grupo')
else:
    print('o nome do homen mais velho é {}'.format(nvelho))
if cont == 0:
    print('Não há mulheres com menos de vinte anos ou mulheres no grupo')
else:
    print('{} mulheres tem menos de 20 anos de idade'.format(cont))
