casa = float(input('Digite o valor da casa R$'))
salario = float(input('Digite o valor do seu salário R$'))
anos = int(input('Em quantos anos pretende pagar? '))*12
parcela = casa / anos
if parcela > (salario*0.7):
    print('Emprestimo negado, parcela exede 30% do salário. Valor da parcela \033[31mR${:.2f}\033[m'.format(parcela))
else:
    print('Emprestimo aceito, Obrigado pela preferência!. Valor da parcela \033[32mR${:.2f}\033[m'.format(parcela))
