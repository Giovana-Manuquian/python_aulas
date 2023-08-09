real = float(input('Quanto de dinheiro você tem para fazer a converção em dólar? R$'))
dolar = real/4.90
print('''
  _____________________
 |  _________________  |
             {}              
 | |_________________| |
 |  ___ ___ ___   ___  |
 | | 7 | 8 | 9 | | + | |
 | |___|___|___| |___| |
 | | 4 | 5 | 6 | | - | |
 | |___|___|___| |___| |
 | | 1 | 2 | 3 | | x | |
 | |___|___|___| |___| |
 | | . | 0 | = | | ÷ | |
 | |___|___|___| |___| |
 |_____________________|
'''.format(real))

print('Com R${:.2f} você pode ter US{:.2f}'.format(real, dolar))