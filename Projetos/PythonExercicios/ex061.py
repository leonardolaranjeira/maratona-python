
print('Exercício 61')

'''Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiro termos da progressão
usando a estrutura while.'''

print('-=' * 20)
print(f'{' ' * 10}PROGRESSÃO ARITMÉTICA{' ' * 10}')
print('-=' * 20)

pri_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))

primeiro = pri_termo - razao
enesimo = pri_termo + (10 - 1) * razao
while primeiro != enesimo:
    primeiro += razao
    print(f'{primeiro} ', end='')

print(f'\nEstes são os 10 primeiros termos da PA com PRIMEIRO TERMO {pri_termo} e RAZÃO {razao}.')

# Desafio concluído
