
print('Exercício 65')

'''Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os 
valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar
a digitar valores.'''

cont = 0
soma = 0
maior = 0
menor = 0

while True:
    num = int(input('Digite um número: (Se quer encerrar, digite "0")\n'))
    cont += 1
    soma += num

    if cont == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor and num != 0:
            menor = num
        if num == 0:
            media = soma / (cont - 1)
            print(f'Foram digitados {cont - 1} valores e a soma destes valores fica {soma}.')
            break

print(f'A média final dos valores digitados é {media:.3}, sendo o maior número digitado o {maior} '
      f'e o menor número digitado o {menor}.')

# Desafio concluído!
