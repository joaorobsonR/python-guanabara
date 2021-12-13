from datetime import date
maior = date.today().year
velho = 0
novo = 0
for c in range(1, 8):
    ano = int(input('Digite o ano do seu {}° pessoa: '.format(c)))
    if maior - ano >= 18:
        velho += +1
    else:
        novo += +1
print('{} pessoas são maiores de idade'.format(velho))
print('{} pessoas são menores de idade'.format(novo))
