# ENUNCIADO
# Um professor quer sortear um dos seus quatro alunos para apagar o quador. Faça um programa que ajude ele,
# lendo o nome dele e escrevendo o nome na tela

import random

aluno = [str(input('Qual o nome do aluno? ')), str(input('Qual o nome do aluno? ')),
         str(input('Qual o nome do aluno? ')), str(input('Qual o nome do aluno? '))]


print('\nO aluno sorteado foi {}!'.format(aluno[random.randint(0, 3)]))
