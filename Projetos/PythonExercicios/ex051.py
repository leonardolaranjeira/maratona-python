
print(f'{' ' * 10}Exercício 51{' ' * 10}')

'''Desenvolva um programa que leia o primeiro termo e a razão de uma Progressão Aritmética (PA). No final, mostre os 10 primeiros termos
dessa progressão.'''

print('-=' * 20)
print(f'{' ' * 10}PROGRESSÃO ARITMÉTICA{' ' * 10}')
print('-=' * 20)

pri_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))

print(f'{pri_termo} ', end='')
total = pri_termo
for p in range(0, 10):
    total += razao
    print(f'{total} ', end='')
print(f'\nEstes são os 10 primeiros termos da PA com PRIMEIRO TERMO {pri_termo} e RAZÃO {razao}.')

# Desafio concluído
