print('Exercício 87')

'''Aprimore o desafio anterior, mostrando no final:
    A) A soma de todos os valores pares digitados.
    B) A soma dos valores da terceira coluna.
    C) O maior valor da segunda linha.'''

print('-=' * 30)
matriz = []
pares = 0
terceira = 0
maior = 0

for l in range(3):
    linha = []
    for p in range(3):
        pos = int(input(f'Digite um valor para a posição [{l}, {p}]: '))
        linha.append([pos])
        if pos % 2 == 0:
            pares += pos
            # Se o valor for PAR, ele será somado e armazenado em uma variável.

        if p == 2:
            terceira += pos
            # soma a terceira coluna.

        if l == 0:
            maior = pos
        elif l == 1 and (p == 0 or p == 1 or p == 2):
            maior = pos
            # Verifica qual o maior valor da segunda linha e armazena em uma variável.
    matriz.append(linha)

print('=-' * 30)
for linha in matriz:
    print(linha[0], linha[1], linha[2])
print('-=' * 30)
print(f'A soma dos valores pares digitados é de: {pares}')
print(f'A soma dos valores da terceira coluna é de: {terceira}')
print(f'O maior valor da segunda linha: {maior}')

# Desafio concluído!
