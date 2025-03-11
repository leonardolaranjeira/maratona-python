
print('Exercício 81')

'''Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
    A) Quantos números foram digitados.
    B) A lista de valores ordenada de forma decrescente.
    C) Se o valor 5 foi digitado e está ou não na lista.'''

cont = 0
numeros = []
cinco = False

while True:
    cont += 1
    num = int(input(f'Digite o {cont}° valor (Digite "999" para parar!): '))
    numeros.append(num)
    if num == 999:
        numeros.pop()
        numeros.sort(reverse=True)
        break
    if num == 5:
        cinco = True

print('-=' * 30)
print(f'Foram digitados: {len(numeros)} números!')
print(f'Os número ordenados de forma decrescente fica: {numeros}')
if cinco:
    print(f'O número 5 está na lista.')
elif not cinco:
    print('O número cinco não está na lista.')
print('-=' * 30)

# Desafio concluído!
