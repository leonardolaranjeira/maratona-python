
print('Exercício 50')

'''Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor
digitado for ímpar, desconsidere-o.'''

total = 0
for n in range(1, 7):
    num = int(input('Escolha seis números: '))
    if num % 2 == 0:
        total += num
print(f'A soma dos valores pares é igual à: {total}.')

# Desafio concluído!
