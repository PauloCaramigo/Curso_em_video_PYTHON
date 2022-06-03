# ENUNCIADO
# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento

salario = float(input('Qual é o seu salário? '))

print('\nPARABÉNS!!!\nVocê ganhou um aumento de salário de 15%!\nSeu novo salário é de R${:.2f}'.format(salario*1.15))
print('\nPARABENS!!!\nVocê ganhou um aumento de salário de 15%!\nSeu novo salário é de R${:.2f}'
      .format(salario + (salario*15/100)))
print('\nPARABÉNS!!!\nVocê ganhou um aumento de salário de 25%!\nSeu novo salário é de R${:.2f}'
      .format(salario + (salario*25/100)))

