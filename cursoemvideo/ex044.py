from time import sleep
produto = float(input('Qual é preço do produto? R$'))
print('''Qual vai ser a forma de pagamento?
[1] Para pagamento avista (dinheiro/cheque) com 10% de desconto.
[2] Para pagamento avista no cartão com 5% de desconto.
[3] Para pagamento em até 2x no cartão preço sem desconto.
[4] Para pagamento em até 3x ou mais com 20% de JUROS.''')
pagmento = float(input('Digite a opção de pagamento desejada: '))
print('Validando opção de pagamento...aguarde...')
sleep(3)
if pagmento == 1:
    produto = produto*0.9
    print(f'Valor a pagar R${produto} Obrigado pela preferensia!')
elif pagmento == 2:
    produto = produto*0.95
    print(f'Valor a pagar R${produto} Obrigado pela preferensia!')
elif pagmento == 3:
    print(f'Valor a pagar R${produto}, em 2x de R${produto/2} Obrigado pela preferensia!')
elif pagmento == 4:
    parcela = int(input('Quantas parecelas será pago? '))
    produto = produto*1.2
    print(f'Valor a pagar R${produto}, em {parcela} parcelas de R${produto/parcela}, Obrigado pela preferensia!')
else:
    print('\033[31mOpçaõ inválida tente novamente\033[m')
