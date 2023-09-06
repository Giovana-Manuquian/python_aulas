while True:
    nome = input('Digite o nome do(a) funcionário(a): ')
    if nome.isalpha():
        break
    else:
        print("Por favor, digite somente letras para o nome.")

salario = float(input('Digite o salário do(a) funcionário(a): '))
novoSalario = salario + (salario * 15 / 100)
print('O salário do(a) funcionário(a) {} era R${:.2f}, com 15% de aumento, passa a ficar R${:.2f}'.format(nome, salario, novoSalario))
