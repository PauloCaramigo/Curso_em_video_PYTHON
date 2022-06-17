# ENUNCIADO
# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalho dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random

n = 0
alunos = []
ordem = []

while n < 4:
    alunos.append(str(input('Qual é o nome do aluno? ')))
    n += 1

while len(ordem) < len(alunos):
    num = random.randint(0, 3)
    if alunos[num] in ordem:
        print('O aluno {} já está na fila!'.format(alunos[num]))
    else:
        print('O aluno {} foi adicionado na fila!'.format(alunos[num]))
        ordem.append(alunos[num])

print('\n{}'.format(ordem))

# Também pode ser feito da seguinte forma

random.shuffle(alunos)

print('\nA ordem de apresentação é \n{}'.format(alunos))
