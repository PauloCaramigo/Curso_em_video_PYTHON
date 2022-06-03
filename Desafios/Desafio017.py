# ENUNCIADO
# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo,
# calcule e mostre o comprimento da hipotenusa.
from math import sqrt, pow

catOpt = float(input('Informe o valor do cateto oposto: '))
catAdj = float(input('Informe o valor do cateto adjacente: '))

hip = sqrt(pow(catOpt, 2) + pow(catAdj, 2))

print('A hipotenusa do seu triângulo retângulo vale {}'.format(hip))
