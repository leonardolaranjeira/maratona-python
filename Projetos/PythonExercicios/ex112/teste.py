from ex112.utilidadescev import dado, moeda

print('Exercício 112')

'''Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado. Crie uma função chamada 
leiaDinheiro() que seja capaz de funcionar como a função input(), mas com uma validação de dados para aceitar apenas 
valores que sejam monetários.'''

p = dado.leiadinheiro('Digite o preço: R$ ')
moeda.resumo(p, 35, 22)

'''
# Verificador monetário
def leiadinheiro(msg):
    vermelho = '\033[1:31m'
    limpa = '\033[m'
    ok = False
    valor = 0.0
    while True:
        i = str(input(msg)).replace(',', '.')
        try:
            valor = float(i)
            ok = True
        except ValueError:
            print(f'{vermelho}Erro! Você digitou um valor inválido.{limpa}')

        if ok:
            break
    return valor
'''

'''
# funcionalidades
def resumo(num, a, d):
    print('-' * 30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-' * 30)
    print(f'Preço analisado: {moeda(num)}')
    print(f'Dobro do preço: {dobro(num, real=True)}')
    print(f'Metade do preço:  {metade(num, real=True)}')
    print(f'35% de aumento: {aumentar(num, a, real=True)}')
    print(f'22% de redução:  {diminuir(num, d, real=True)}')
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
