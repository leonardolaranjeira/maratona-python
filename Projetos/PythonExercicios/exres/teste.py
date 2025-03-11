from exres.utilidadescev import moeda, dados

print('Resolução do exercício 112')

'''Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado. Crie uma função chamada 
leiaDinheiro() que seja capaz de funcionar como a função input(), mas com uma validação de dados para aceitar apenas 
valores que sejam monetários.'''

p = dados.leiadinheiro('Digite o preço: R$')
moeda.resumo(p, 35, 22)

'''
# Função para verificar se o valor é válido.
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
def aumentar(preco=0, taxa=0, format=False):
    res = preco + (preco * taxa / 100)
    return res if format is False else moeda(res)


def diminuir(preco=0, taxa=0, format=False):
    res = preco - (preco * taxa / 100)
    return res if format is False else moeda(res)


def dobro(preco=0, format=False):
    res = preco * 2
    return res if not format else moeda(res)


def metade(preco=0, format=False):
    res = preco / 2
    return res if not format else moeda(res)


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:>.2f}'.replace('.', ',')


def resumo(preco=0, taxaa=10, taxar=5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
    print(f'{taxaa}% de aumento: \t{aumentar(preco, taxaa, True)}')
    print(f'{taxar}% de redução: \t{diminuir(preco, taxar, True)}')
    print('-' * 30)

'''

# Desafio corrigído!
