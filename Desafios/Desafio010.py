# ENUNCIADO
# Crie um programa que leia quanto uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
# US$ 1.00 = R$ 3,27

valor = float(input('Quantos reais vc tem na carteira? R$'))

print('O valor que você tem em dolar é US${:.2f}'.format(valor/4.8))
print('O valor que você tem em rublo russo é {:.2f}₽'.format(valor/0.076))
