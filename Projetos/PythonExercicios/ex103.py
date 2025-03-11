
print('Exercício 103')

'''Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e 
quantos dols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido
informado corretamente.'''

def ficha(nome='<desconhecido>', gols=0):
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')

jogador = str(input('Nome do jogador: ')).strip()
valor = str(input('Número de gols: ')).strip()

if valor == '':
    valor = 0
else:
    valor = int(valor)

if jogador == '':
    jogador = '<desconhecido>'

ficha(jogador, valor)

# Desafio concluído 90%!
