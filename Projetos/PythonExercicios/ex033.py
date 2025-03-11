
print('Exercício 33')

'''Faça um programa que leia três números e mostre qual é o maior e qual é o menor.'''

print('Qual dos 3 números é o maior?')

a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))

print('Os números escolhidos foram: {}, {} e {}!'.format(a, b, c))

# Verificando quem é menor:
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

# Verificando quem é maior:
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print('O maior valor escolhido foi: {}!'.format(maior))
print('O menor valor escolhido foi: {}!'.format(menor))

# Desafio concluído!
