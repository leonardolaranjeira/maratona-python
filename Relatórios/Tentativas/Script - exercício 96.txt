
print('Exercício 96')

'''Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular 
(largura e comprimento) e mostre a área do terreno.'''


def area():
    print('-' * 40)
    print(f'{'CONTROLE DE TERRENOS':^40}')
    print('-' * 40)

    lar = float(input('Largura (M): '))
    comp = float(input('Comprimento (M): '))
    dimensoes = lar * comp
    print(f'A área de um terreno {lar:.2f} x {comp:.2f} é de {dimensoes}m²')


area()

# Desafio concluído!
