
print('Exercício 60')

'''Faça um programa que leia um número qualquer e mostre o seu fatorial.
Ex: 5! = 5x4x3x2x1 = 120 (Tente fazer com WHILE e com FOR)'''

print('Cálculo de fatorial!')

num = int(input('Digite um número qualquer: '))

'''fatorial = 1
for f in range(num, 0, -1):
    if f == 1:
        print(f, end='')
    else:
        print(f'{f} x ', end='')
        fatorial *= f

print(f' = {fatorial}')

print(f'O fatorial de {num} é {fatorial}.')'''

fatorial = 1
f = num
while num >= 1:
    if num == 1:
        print(num, end='')
    else:
        print(f'{num} x ', end='')
    fatorial *= num
    num -= 1

print(f' = {fatorial}')
print(f'O fatorial de {f} é {fatorial}.')

# Desafio parcialmente concluído!
