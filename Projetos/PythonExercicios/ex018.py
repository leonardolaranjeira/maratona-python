from math import radians, sin, cos, tan

print('Exercício 18')

# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

print('Seno, cosseno e tangente!')

ang = float(input('Digite o ângulo que você deseja: '))

seno = sin(radians(ang))
print('O ângulo de {} tem o SENO de {:.2f}'.format(ang, seno))
coss = cos(radians(ang))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(ang, coss))
tang = tan(radians(ang))
print('O ângulo de {} tem o TANGENTE de {:.2f}'.format(ang, tang))

# Desafio concluído!
