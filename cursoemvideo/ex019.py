import random

aluno1 = str(input('digite o nome do aluno: '))
aluno2 = str(input('digite o nome do aluno: '))
aluno3 = str(input('digite o nome do aluno: '))
aluno4 = str(input('digite o nome do aluno: '))
nomes = [aluno1, aluno2, aluno3, aluno4]
print(f'o aluno escolhido é {random.choice(nomes)}')
