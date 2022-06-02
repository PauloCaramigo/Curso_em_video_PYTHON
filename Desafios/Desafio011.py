# ENUNCIADO
# Faça um programa que leia a largura e altura de uma parede em metros, calcule a sua área e a quantidade
# de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m²

alt = float(input('Quantos metros de altura tem a parede? '))
lar = float(input('Quantos metros de largura tem a parede? '))
area = alt*lar

print('\nA área quadrada da parede é de {} e sera necessario {} litros de tinta para pintar a parede'
      .format(area, area/2))
