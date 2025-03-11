
print('Exercício 70')

'''Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai 
continuar. No final, mostre:
A) Qual é o total gasto na compra.
B) Quantos produtos custam mais de R$1000.
C) Qual é o nome do produto mais barato.'''

soma = maior_mil = cont = menor = 0
decisao = nome_menor = ''
while True:
    print('-' * 30)
    print(f'{'LOJÃO DO LEO': ^30}')
    print('-' * 30)

    produto = str(input('Digite o nome do produto: ')).strip().capitalize()
    preco = float(input('Digite o preço do produto: R$'))
    soma += preco
    cont += 1

# Verifica se o produto custa mais do que mil e contabiliza mais 1.
    if preco > 1000:
        maior_mil += 1
    # Está parte está dando bug.

# Verifica se é o menor preço da lista e verifica também qual o nome do produto mais barato.
    if cont == 1:
        menor = preco
        nome_menor = produto
    elif preco < menor:
        menor = preco
        nome_menor = produto

    decisao = str(input('Você quer continuar? [S/N]\n>> ')).strip().upper()[0]
    while decisao != 'S' and decisao != 'N':
        print('Opção inválida, Tente novamente.')
        decisao = str(input('Você quer continuar? [S/N]\n>> ')).strip().upper()[0]
    if decisao == 'N':
        print('Encerrando programa...')
        break

print(f'O total da compra foi R${soma}.')
print(f'Temos {maior_mil} produtos custando mais de R$1000,00.')
print(f'O produto mais barato foi {nome_menor} que custa R${menor:.2f}.')

# Desafio concluído!
