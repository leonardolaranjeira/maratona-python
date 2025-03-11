
print(f'{'Exercício 86':^60}')

'''Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No final, mostre 
a matriz na tela, com a formatação correta.'''

print('-=' * 30)
matriz = []

for l in range(3):
    linha = []
    for p in range(3):
        pos = [int(input(f'Digite um valor para a posição [{l}, {p}]: '))]
        linha.append(pos)
    matriz.append(linha)

print('=-' * 30)
for linha in matriz:
    print(linha[0], linha[1], linha[2])

# Desafio concluído com ajuda!
