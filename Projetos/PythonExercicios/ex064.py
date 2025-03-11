from time import sleep
print('Exercício 64')

'''Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o 
valor 999 (número 'flag'), que é a condição de parada. No final, mostre quantos números foram digitados e qual foi 
a soma entre eles (desconsiderando o flag).'''

cont = 0
soma = 0

while True:
    num = int(input('Digite um número (Para parar digite "999"): '))
    print(f'Você digitou {num}.')
    cont += 1
    if num == 999:
        print('Encerrando programa...')
        sleep(2)
        break
    if num > 0:
        soma += num

print(f'O usuário digitou {cont - 1} números diferentes e a soma entre eles é de {soma}.')

# Desafio concluído!
