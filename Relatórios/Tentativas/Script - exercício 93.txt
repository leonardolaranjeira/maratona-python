
print('Exercício 93')

'''Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e
quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será 
guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.'''

tot_gols = 0

jogador = {'nome': str(input('Qual o nome do jogador? '))}
jogador['partidas'] = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
jogador['gols'] = []

print('-=' * 30)
for c in range(jogador['partidas']):
    gols = int(input(f'Quantos gols na partida {c + 1}? '))
    jogador["gols"].append(gols)
    tot_gols += gols

print('-=' * 30)
print(f'O campo nome tem o valor: {jogador["nome"]}')
print(f'O campo gol tem os valores: {jogador["gols"]}')
print(f'O campo total tem o valor: {tot_gols}')

print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {jogador["partidas"]} partidas.')
for p, g in enumerate(jogador["gols"]):
    print(f'> Na partida {p + 1}, fez {g} gols.')
print(f'Foi um total de {tot_gols} gols.')

# Desafio concluído!
