print('*'*30)
print('{:^30}'.format('BANCO DO JOÃO'))
print('*'*30)
valor = int(input('De quantos será o saque? '))
notas50 = notas20 = notas10 = notas1 = resto = 0

while True:
    if valor != 0:
        notas50 = valor // 50
        resto = valor - (notas50 * 50)

        notas20 = resto // 20
        resto = resto - (notas20 * 20)

        notas10 = resto // 10
        resto = resto - (notas10 * 10)

        notas1 = resto // 1
        resto = resto - (notas1 * 1)

    if resto == 0:
        break

print(f'As notas para o saque serão\n'
      f'{notas50} notas de 50\n'
      f'{notas20} notas de 20\n'
      f'{notas10} notas de 10\n'
      f'{notas1} notas de 1\n')
print('num total de {} notas'.format(notas50 + notas20 + notas10 + notas1))
