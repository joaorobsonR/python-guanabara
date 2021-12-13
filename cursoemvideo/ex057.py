sexo = ''
while sexo != 'F' and sexo != 'M':
    sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()[0]
    if 'F' or 'M' in sexo:
        print('Cadastro válido!')
    else:
        print('Registro inválido tente novamente!')
print('Registro feito com sucesso \033[31m{}\033[m'.format(sexo))
