# ENUNCIADO
# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo
import math

angulo = int(input('Informe um ângulo: '))

cosseno = math.cos(angulo)
seno = math.sin(angulo)
tangente = math.tan(angulo)

print('O cosseno do ângulo {}º equivale a {:.3f} radianos.'.format(angulo, cosseno))
print('O seno do ângulo {}º equivale a {:.3f} radianos.'.format(angulo, seno))
print('A tangente do ângulo {}º equivale a {:.3f} radianos.'.format(angulo, tangente))
