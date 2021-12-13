print('\033[32m=-=\033[m'*18)
peso = float(input('Digite seu peso: '))
atura = float(input('Digite sua altura: '))
imc = (peso / (atura*atura))
if imc <= 18.5:
    print(f'Abaixo do peso, imc {imc:.2f}')
elif imc <= 25:
    print(f'Peso ideal, imc {imc:.2f}')
elif imc <= 30:
    print(f'Sobrepeso CUIDADO, imc {imc:.2f}')
elif imc <= 40:
    print(f'\033[31mOBESIADADE, imc {imc:.2f}!\033[m')
else:
    print(f'\033[31mObsedidade mórbida procure um MÉDICO, imc {imc:.2f}\033[m!')
print('\033[32m=-=\033[m'*18)
