# ENUNCIADO
# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.
from math import floor

num = float(input('Informe um número real: '))

print('Sua porção inteira é de {}'.format(floor(num)))
