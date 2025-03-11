
print('Exercício 71')

'''Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor
a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.'''

print('=' * 50)
print(f'{'BANCO TORANJO': ^50}')
print('=' * 50)

valor = int(input('Qual valor você quer sacar? R$ '))

notas_50 = notas_20 = notas_10 = notas_1 = 0
while valor >= 50:
    valor -= 50
    notas_50 += 1

while valor >= 20:
    valor -= 20
    notas_20 += 1

while valor >= 10:
    valor -= 10
    notas_10 += 1

while valor >= 1:
    valor -= 1
    notas_1 += 1


print(f'Foram utilizadas {notas_50} notas de R$50.')
print(f'Foram utilizadas {notas_20} notas de R$20.')
print(f'Foram utilizadas {notas_10} notas de R$10.')
print(f'Foram utilizadas {notas_1} notas de R$1.')

print('Volte sempre ao BANCO TORANJO!\nTenha um bom dia!')

# Desafio concluído com ajuda!
