item = input('Digite algo: ')
print('O tipo primitivo desse valor é: ', type(item))
print('Tem espaços? ', item.isspace())
print('É um número? ', item.isnumeric())
print('É alfabético? ', item.isalpha())
print('É alfanúmerico? ', item.isalnum())
print('Está em maiúsculas? ', item.isupper())
print('Está em minúsculas? ', item.islower())
print('Está capitalizada? ', item.istitle())
