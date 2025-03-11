from random import randint

print(f'{'Exercício 100':^80}')

'''Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função
vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores 
PARES sorteados pela função anterior.'''

soma = 0
numeros = []


def sorteia():
    for n in range(0, 5):
        numero = randint(1, 50)
        numeros.append(numero)


sorteia()


def somapar():
    global soma
    for p in numeros:
        if p % 2 == 0:
            soma += p


somapar()

print('-=' * 40)
print(f'Sorteando 5 valores da lista: ', end='')
for num in numeros:
    print(f'{num} ', end='')
print()

print(f'Somando os valores pares de {numeros} temos: {soma}')
print('-=' * 40)

# Desafio concluído!
