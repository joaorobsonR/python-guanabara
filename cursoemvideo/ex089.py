alunos = []
notas = []
cont = 0
while True:
    notas.append([])
    alunos.append(input('digite o nome do aluno: '))
    if cont >= 0:
        for c in range(1, 3):
            notas[cont].append(int(input(f'Nota {c}:')))
    cont += 1
    resp = str(input('deseja continuar? '))
    if resp in 'Nn':
        break
print('-'*40)
for a , p in enumerate(alunos):
    print(f'{a}° {p},    media = {sum(notas[a])/2}')
print('-'*40)

while True:
    verificar = int(input('verificar a nota de qual aluno? digite o numero (999 para parar) '))
    if verificar == 999:
        break
    print(f'aluno {alunos[verificar]} tirou as notas {notas[verificar]}')
