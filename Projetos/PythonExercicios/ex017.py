from math import hypot
print('Exercício 17')

# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e
# mostre o comprimento da hipotenusa.

print('Calculo da hipotenusa!')

co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
hi = hypot(ca, co)

print('A soma dos quadrados dos catetos equivalem a: {:.2f}'.format(hi))

# Desafio concluído!
