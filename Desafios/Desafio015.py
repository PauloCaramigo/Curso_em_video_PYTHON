# ENUNCIADO
# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias
# pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por km
# rodado.

dia = int(input('Por quantos dias o carro foi alugado? '))
km = float(input('Quantos km foi rodado com o carro? '))
preco = (60*dia) + (0.15*km)

print('O valor a ser pago é de R${:.2f}'.format(preco))
