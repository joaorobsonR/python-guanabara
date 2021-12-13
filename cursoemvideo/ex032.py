from datetime import date
ano = int(input('\033[33mDigite o ano que se deseja verficar: '))
if ano == 0:
    ano = date.today().year
if (ano%4 == 0 and ano%100 != 0) or (ano%4 != 0 and ano%400 == 0):
    print('O ano {} é bissexto'.format(ano))
else:
    print('O ano {} não é bissexto'.format(ano))
print('\033[31mFIM!!!')
