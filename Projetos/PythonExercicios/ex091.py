from random import randint
from time import sleep

print('Exercício 91')

'''Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados 
em um dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.'''

jogadores = {}

print(f'{'VALORES SORTEADOS':^60}')
for j in range(1, 5):
    jogadores[f'jogador {j}'] = randint(1, 6)

for p in range(1, 5):
    print(f'O jogador {p} jogou: {jogadores[f'jogador {p}']}')
    sleep(1)

print('=-' * 30)
print('As jogadas foram: ', end='')
for j in jogadores:
    print(jogadores[j], end=' ')

print()
print('-=' * 30)
print(f'{'RANKING DOS JOGADORES':^60}')

# Ordenar os jogadores com base nos valores
ordem = sorted(jogadores.items(), key=lambda item: item[1], reverse=True)

for i, (jogador, valor) in enumerate(ordem, start=1):
    print(f'{i}° lugar: {jogador} tirou {valor} no dado.')
    sleep(1)

# Desafio concluído com ajuda!
