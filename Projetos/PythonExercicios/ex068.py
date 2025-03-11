from random import randint
from time import sleep

verdeB = '\033[1:32m'
vermelhoB = '\033[1:31m'
amareloB = '\033[1:33m'
limpa = '\033[m'

print('Exercício 68')

'''Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador PERDER, 
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo'''

cont = 0
pc = ''
while True:
    computador = randint(1, 50)
    print('=-' * 30)
    print(f'{verdeB}{f'{vermelhoB}PAR {amareloB}OU {verdeB}IMPAR{amareloB}?': ^60}{limpa}')
    print('=-' * 30)
    print(f'Para encerrar digite um valor {vermelhoB}NEGATIVO!{limpa}')
    num = int(input('Escolha um número: '))
    if num < 0:
        print(f'{vermelhoB}Encerrando programa...{limpa}')
        sleep(2)
        break

    jogador = str(input(f'{vermelhoB}PAR {amareloB}OU {verdeB}IMPAR{amareloB}? '
                        f'{verdeB}[{vermelhoB}P{limpa}{amareloB}/{verdeB}I{limpa}{verdeB}]: {limpa}')).strip().upper()[0]
    print('=-' * 30)

    if jogador == 'P':
        pc = 'I'
    elif jogador == 'I':
        pc = 'P'

    soma = num + computador
    par = soma % 2
    if jogador == 'P' and par == 0:
        print(f'{verdeB}VOCÊ VENCEU!!!{limpa}')
        print(f'O jogador escolheu {num} e o computador {computador}. Total de {soma} (DEU PAR).')
        cont += 1
    elif jogador == 'I' and par != 0:
        print(f'{verdeB}VOCÊ VENCEU!!!{limpa}')
        print(f'O jogador escolheu {num} e o computador {computador}. Total de {soma} (DEU IMPAR).')
        cont += 1
    elif pc == 'P' and par == 0:
        print(f'{vermelhoB}VOCÊ PERDEU!!!{limpa}')
        print(f'O jogador escolheu {num} e o computador {computador}. Total de {soma} (DEU PAR).')
        break
    elif pc == 'I' and par != 0:
        print(f'{vermelhoB}VOCÊ PERDEU!!!{limpa}')
        print(f'O jogador escolheu {num} e o computador {computador}. Total de {soma} (DEU IMPAR).')
        break
    elif jogador not in ['I', 'P']:
        print(f'{vermelhoB}Opção inválida. Tente novamente!!!{limpa}')

print(f'{amareloB}GAME OVER!!!{limpa}\nVocê venceu {cont} vez(es).')
sleep(2)

# Desafio concluído!
