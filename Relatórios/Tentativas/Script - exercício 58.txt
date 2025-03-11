from random import randint
from time import sleep
print('Exercício 58')

'''Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador 
vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.'''


print('-=-' * 20)
print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
print('-=-' * 20)

computador = randint(0, 10)
jogador = ''
cont = 0
while jogador != computador:
    sair = str(input('Quer continuar? [S/N]\n')).upper()[0].strip()
    if sair == 'N':
        print(f'Você desistiu após {cont} palpite(s).')
        break
    if sair != 'S' and sair != 'N':
        print('Está não é uma opção válida!')
    else:
        jogador = int(input('Em que número eu pensei?\n'))
        cont += 1
        print('PROCESSANDO...')
        sleep(1)
        if jogador == computador:
            print(f'PARABÉNS!\nEu também escolhi {computador}... Você me venceu com {cont} palpite(s)!')
        else:
            print('GANHEI!\nHAHAHA, tente de novo!')

# Desafio concluído!
