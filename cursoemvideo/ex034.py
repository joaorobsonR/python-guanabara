salario = float(input('Digite o valor do seu salário '))
if salario <= 1250:
    print('O aumento do seu salário é de 15% será reajustado para {:.2f}'.format(salario*1.15))
else:
    print('O aumento do seu salário é de 10% será reajustado para {:.2f}'.format(salario*1.1))
