nome = str(input('Digite seu nome: ')).title().strip()
nome = nome.split()
print('Primeiro nome: ', nome[0])
print('Ultimo nome: {}'.format(nome[-1]))
