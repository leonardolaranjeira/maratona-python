print('-=' * 30)
print(f'{"Exercício 66": ^60}')
print('-=' * 30)

'''Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar
o valor "999", que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles
(desconsiderando o flag).'''

cont = soma = 0
while True:
    num = int(input('Digite um número (Para parar digite "999"): '))
    if num == 999:
        print('Encerrando...')
        break
    cont += 1
    soma += num
print('=-' * 30)
print(f'Foram digitados {cont} números e a soma entre eles é igual a: {soma}.')

# Desafio concluído!
