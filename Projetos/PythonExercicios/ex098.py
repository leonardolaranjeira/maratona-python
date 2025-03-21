from time import sleep

print('Exercício 98')

'''Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo e realize a
contagem. Seu programa tem que realizar três contagens através da função criada:

A) De 1 até 10, de 1 em 1
B) De 10 até 0, de 2 em 2
c) Uma contagem personalizada.'''


def contador():
    print('-=' * 34)
    print('Contagem de 1 até 10 de 1 em 1.')
    for n in range(1, 10):
        sleep(1)
        print(f'{n} ', end='')
    print('FIM!')

    print('-=' * 34)
    print('contagem de 10 até 0 de 2 em 2.')
    for n in range(10, -1, -2):
        sleep(1)
        print(f'{n} ', end='')
    print('FIM!')

    print('-=' * 34)
    print('Agora é sua vez de personalizar a contagem!')
    i = int(input('Defina o início da contagem: '))
    f = int(input('Defina o fim da contagem: '))
    p = int(input('Defina o passo da contagem: '))
    print('-=' * 34)
    print(f'Contagem de {i} até {f} de {p} em {p}.')
    if p > 0:
        for n in range(i, f + 1, p):
            sleep(1)
            print(f'{n} ', end='')
    else:
        for n in range(i, f - 1, p):
            sleep(1)
            print(f'{n} ', end='')
    print('FIM!')


contador()

# Desafio incompleto!
