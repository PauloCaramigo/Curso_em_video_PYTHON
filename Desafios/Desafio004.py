msg = input('Digite algo: ')

print('O tipo primitivo é ', type(msg))
print('Só tem espaços? ', msg.isspace())
print('É um númerico? ', msg.isnumeric())
print('É alfabético? ', msg.isalpha())
print('É alfanumérico? ', msg.isalnum())
print('Está em maiúsculas? ', msg.isupper())
print('Está em minúsculas? ', msg.islower())
print('Está capitalizada? ', msg.istitle())