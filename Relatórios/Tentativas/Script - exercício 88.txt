from random import randint
from time import sleep

print('Exercício 88')

'''Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos
serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.'''

print('--' * 30)
print(f'{'JOGA NA MEGA SENA':^60}')
print('--' * 30)

qtde = int(input('Quantos jogos você quer que eu sorteie? '))
print()
print(f'{'=-' * 10}{f' SORTEANDO {qtde} JOGOS '}{'-=' * 10}')

for j in range(qtde):
    jogo = []
    for num in range(0, 6):
        numero = randint(1, 60)
        jogo.append(numero)
    print(f'Jogo {j + 1}: {jogo}')
    sleep(1)

print(f'{'=-' * 10}{' < BOA SORTE! > '}{'-=' * 10}')

# Desafio concluído!
