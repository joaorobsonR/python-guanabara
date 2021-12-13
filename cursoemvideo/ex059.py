from time import sleep
opcao = 0
n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
while opcao != 5:
    print('''\033[32m
[1] Somar:
[2] Multiplicar
[3] Maior
[4] Mudar numeros
[5] Sair
    \033[m''')
    sleep(3)
    opcao = int(input('Digite a opção: '))
    if opcao == 1:
        print('A soma de {} + {} = {}'.format(n1, n2, (n1+n2)))
    elif opcao == 2:
        print('A multiplicação de {} x {} = {}'.format(n1, n2, (n1*n2)))
    elif opcao == 3:
        if n1 > n2:
            print('O primeiro é maior {} do que o segundo {}'.format(n1, n2))
        elif n1 == n2:
            print('Os numeros são iguais {} e {}'.format(n1, n2))
        else:
            print(('O segundo {} é maior que o primeiro {}'.format(n2, n1)))
    elif opcao == 4:
        n1 = int(input('Digite o novo primeiro numero: '))
        n2 = int(input('Digite o novo segundo numero: '))
        print('Os novos numero são primeiro {} segundo {}'.format(n1, n2))
    elif opcao == 5:
        print('SAIU, obrigado por utilizar o programa!')
    else:
        print('Operação inválida, tente novamente')
    sleep(5)
print('Fim')
