
print('Exercício 52')

'''Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.'''

num = int(input('Digite um número inteiro: '))

div = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[1:32m', end='')
        div += 1
    else:
        print('\033[1:31m', end='')
    print(f'{c} ', end='')

print(f'\n{'\033[m'}O número {num} foi divisível {div} vez(es).')

if div == 2:
    print(f'E por isso, {'\033[1:32m'}ELE É{'\033[m'} primo!')
else:
    print(f'E por isso, ele {'\033[1:31m'}NÃO É{'\033[m'} primo!')

# Desafio concluído
