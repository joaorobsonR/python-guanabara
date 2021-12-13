cont = contM = contF = 0
sexo =' '
while True:
    print('=-='*10)
    print('CADASTRO DE PESSOA')
    print('=-='*10)
    idade = int(input('idade: '))
    if idade >= 18:
        cont += 1
    while True:
            sexo = str(input('sexo [M/F]: ')).strip().upper()
            if sexo == 'M' or sexo == 'F':
                break

    if sexo == 'M':
        contM += 1
    elif sexo == 'F' and idade < 18:
        contF += 1
    while True:
            verifica = str(input('deseja continuar [S/N]: ')).strip().upper()
            if verifica == 'S' or verifica == 'N':
                break

    if verifica == 'N':
        break

print('pessoas com mais de 18 anos são, {}'.format(cont))
print('homens cadatrados são, {}'.format(contM))
print('mulheres com menos de 18 anos são, {}'.format(contF))
print('\n\033[32mFIM\033[m')
