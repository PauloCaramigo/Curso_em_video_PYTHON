# ENUNCIADO
# Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milímetros

num = float(input('Digite o valor da distancia em metros: '))

print('O valor {}m em decâmetro é {}dam, em hectônetro é {}hm e em quilômetro é {}km'
      .format(num, num*0.1, num*0.01, num*0.001))
print('O valor {}m em decímetro é {}dm, em centímetro {}cm e em milímetros é {}mm.'
      .format(num, num*10, num*100, num*1000))
