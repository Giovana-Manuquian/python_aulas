print('-----------------------------------------------------------------------------------')
n =input(('Digite o nome do(a) aluno(a) para saber a média: '))
n1 = float(input('Primeira nota do(a) aluno(a) {}: '.format(n)))
n2 = float(input('Segunda nota do(a) aluno(a) {}: '.format(n)))
media = (n1 + n2) / 2
print('A média do(a) aluno(a) {} entre {} e {} é: {:.1f}'.format(n, n1, n2, media))
print('-----------------------------------------------------------------------------------')