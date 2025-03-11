
print('Exercício 48')

'''Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três
e que se encontram no intervalo de 1 até 500.'''

total = 0
cont = 0
for n in range(1, 501, 2):
    if n % 3 == 0:
        total += n
        cont += 1
print(f'A soma dos {cont} valores entre 1 e 500 divisíveis por 3 é de {total}.')

# Desafio concluído!
