from datetime import date
ano = int(input('Em que ano você nasceu? '))
idade = date.today().year - ano
if idade < 18:
    mod = abs(idade-18)
    print('Ainda não é hora de se alistar faltam {} anos \033[32m GOOD BOY!!!\033[m'.format(mod))
    print('Seu alistamento será em {}'.format(mod + (date.today().year)))
elif idade == 18:
    print('É hora de se alistar, \033[32mdiriga-se a junta militar e aliste-se!!!\033[m')
else:
    print('Era para você ter se alistado há {} anos, \033[31mBAD BOY!!!\033[m'.format(idade-18))
    print('Seu alistamento foi em {}'.format((date.today().year) - idade + 18))
