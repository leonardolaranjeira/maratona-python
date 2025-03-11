from datetime import datetime

vermelho_B = '\033[1:31m'
amarelo_B = '\033[1:33m'
verde_B = '\033[1:32m'
limpa = '\033[m'

print('Exercício 101')

'''Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma 
pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.'''

def voto(nasc):

    ano_atual = datetime.now().year
    idade = ano_atual - nasc

    if idade < 16:
        print(f'Com {idade} anos: {vermelho_B}VOTO NEGADO{limpa}')
    elif 16 <= idade < 18 or idade > 70:
        print(f'Com {idade} anos: {amarelo_B}VOTO OPCIONAL{limpa}')
    else:
        print(f'Com {idade} anos: {verde_B}VOTO OBRIGATÓRIO{limpa}')


ano = int(input('Em que ano você nasceu? '))

voto(ano)

# Desafio concluído!
