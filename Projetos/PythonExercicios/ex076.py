
print('Exercício 76')

'''Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços na sequência. No final,
mostre uma listagem de preços, organizando os dados em forma tabular.'''

listagem = ('LEITE', 6.38, 'CEREAL', 8.52, 'BISCOITO', 3.63, 'VINHO', 9.99, 'ARROZ', 5.89, 'FEIJAO', 6.54,
            'BANANA', 4.33, 'OLEO', 8.20, 'LIMAO', 3.50, 'SALGADINHO', 4.50)


print('-' * 40)
print(f'{'Lista de preços':^40}')
print('-' * 40)

for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')
print('-' * 40)

# Desafio concluído!
