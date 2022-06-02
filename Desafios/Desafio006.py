# ENUNCIADO
# Crie um algoritmo que leia um número e mostre o seu dobro, trilo e raiz quadrada.

num = float(input('Digite algum número: '))

print('O dobro de {} é {}, seu triplo é {} e sua raiz quadrada é {:.2f}.'.format(num, num*2, num*3, num**(1/2)))
