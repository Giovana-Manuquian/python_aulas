while True:
    nomeProduto = input('Digite o nome do produto: ')
    if nomeProduto:
        break
    else:
        print("Por favor, digite um nome válido.")

while True:
    try:
        precoProduto = float(input('Digite o valor do produto: R$'))
        break
    except ValueError:
        print("Por favor, digite um valor numérico válido.")

pagamentoVista = precoProduto - (precoProduto * 5 / 100)
pagamentoParcelado = precoProduto + (precoProduto * 5 / 100)

while True:
    pagamento = input("Digite 'vista' para pagamento à vista ou 'parcelado' para pagamento parcelado: ")
    if pagamento == 'vista':
        print('O produto {} com valor de R${:.2f} à vista fica R${:.2f} com 5% de desconto.'.format(nomeProduto, precoProduto, pagamentoVista))
        break
    elif pagamento == 'parcelado':
        print('Caso seja parcelado, o valor fica R${:.2f} com 5% de juros.'.format(pagamentoParcelado))
        break
    else:
        print("Opção inválida. Digite 'vista' ou 'parcelado'.")
