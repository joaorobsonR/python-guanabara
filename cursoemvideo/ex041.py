from datetime import date
ano = int(input('Ano de nascimento: '))
idade = date.today().year - ano
print('o aluno tem {} anos'.format(idade))
if idade <= 9:
    print('MIRIM')
elif idade <= 14:
    print('INFANTIL')
elif idade <= 19:
    print('JUNIOR')
elif idade <= 25:
    print('SENIOR')
else:
    print('MASTER')
# não precisa colocar 10 <= idade <=14 porque um elfi exclui a possibilidade de dois resultados
