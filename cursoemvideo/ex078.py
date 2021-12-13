from random import randint

listaDigitar = []
listaRandom = []

while True:
    try:
        opcao = int(input('Digite 1 ou 2 para informar os dados:\n'
                          'digitar(1) ou sortear(2) os numeros? '))

        if opcao == 1:
            for i in range(0, 5):
                resp = int(input('digite um numero de 0 até 20: '))
                listaDigitar.append(resp)
            print(f'o maior valor da lista é {max(listaDigitar)}')
            print(f'o menor valor da lista é {min(listaDigitar)}')
            print('o maior valor foi digitado na posição')
            for pos in range(0, len(listaDigitar)):
                if listaDigitar[pos] == max(listaDigitar):
                    print(f'{pos}...', end='')
            print('\no menor valor foi digitado na posição')
            for pos in range(0, len(listaDigitar)):
                if listaDigitar[pos] == min(listaDigitar):
                    print(f'{pos}...', end='')
            print('\n', listaDigitar)

        elif opcao == 2:
            for i in range(0, 5):
                listaRandom.append(randint(0, 20))
            print(f'o maior valor da lista é {max(listaRandom)}')
            print(f'o menor valor da lista é {min(listaRandom)}')
            print('o maior valor foi digitado na posição')
            for pos in range(0, len(listaRandom)):
                if listaRandom[pos] == max(listaRandom):
                    print(f'{pos}...', end='')
            print('\no menor valor foi digitado na posição')
            for pos in range(0, len(listaRandom)):
                if listaRandom[pos] == min(listaRandom):
                    print(f'{pos}...', end='')
            print('\n', listaRandom)
    except:
        print('Erro catastrófico!!!')

    while True:
        conf = str(input('deseja continuar? Sim ou Não: ')).lower().strip()
        if conf == 'sim' or conf == 'não':
            break
    if conf == 'não':
        break
print('\033[32mFIM\033[m')
