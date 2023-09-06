from math import radians, sin, cos, tan
angulo = float(input('Digite o ângulo que de você deseja calcular: '))
seno = sin(radians(angulo))
print('O ângulo de {} tem o SENO de {:.2f}'.format(angulo, seno))
cosseno = cos(radians(angulo))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(angulo, cosseno))
tangente = tan(radians(angulo))
print('o ângulo de {} tem a TANGENTE de {:.2f}'.format(angulo, tangente))