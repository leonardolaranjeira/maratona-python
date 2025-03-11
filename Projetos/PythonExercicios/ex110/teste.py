import moeda

print('Exercício 110')

'''Adcione ao módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(), que mostre na tela algumas
informaões geradas pelas funções que já temos no módulo criado até aqui.'''

p = float(input('Digite o preço: R$ '))
moeda.resumo(p, 80, 35)

'''

def resumo(num, a, d):
    print('-' * 30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-' * 30)
    print(f'Preço analisado: {moeda(num)}')
    print(f'Dobro do preço: {dobro(num, real=True)}')
    print(f'Metade do preço: {metade(num, real=True)}')
    print(f'80% de aumento: {aumentar(num, a, real=True)}')
    print(f'35% de redução: {diminuir(num, d, real=True)}')
    print('-' * 30)


def moeda(num):
    mone = f'R$ {num:.2f}'
    return mone


def aumentar(num, p, real=False):
    por = (p / 100)
    if real:
        aum = f'R$ {num + (por * num):.2f}'
    else:
        aum = num + (por * num)
    return aum


def diminuir(num, p, real=False):
    por = (p / 100)
    if real:
        dim = f' R$ {num - (por * num):.2f}'
    else:
        dim = num - (por * num)
    return dim


def dobro(num, real=False):
    if real:
        dob = f' R$ {(num * 2):.2f}'
    else:
        dob = num * 2
    return dob


def metade(num, real=False):
    if real:
        met = f' R$ {(num / 2):.2f}'
    else:
        met = num / 2
    return met
    '''

# Desafio concluído!
