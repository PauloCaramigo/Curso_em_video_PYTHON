# ENUNCIADO
# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.

preco = float(input('Qual o valor do produto? '))

print('O novo valor do seu produto com 5% de desconto é de {:.2f}!'.format(preco*0.95))
print('O novo valor do seu produto com 5% de desconto é de {:.2f}!'.format(preco - (preco*5/100)))
print('O novo valor do seu produto com 10% de desconto é de {:.2f}!'.format(preco - (preco*10/100)))
print('O novo valor do seu produto com 27% de desconto é de {:.2f}!'.format(preco - (preco*27/100)))
