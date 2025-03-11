
print('Exercício 56')

'''Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
    - A média de idade do grupo.
    - Qual o nome do homem mais velho.
    - Quantas mulheres têm menos de 20 anos.'''

soma_idade = 0
media_idade = 0
maior_idade_homem = 0
nome_velho = ''
tot_mulher_20 = 0

for ps in range(1, 5):
    print(f'{'-' * 5} {ps}ª PESSOA {'-' * 5}')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()

    soma_idade += idade

    if ps == 1 and sexo in 'Mm':
        maior_idade_homem = idade
        nome_velho = nome

    if sexo in 'Mm' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_velho = nome

    if sexo in 'Ff' and idade < 20:
        tot_mulher_20 += 1

media_idade = soma_idade / 4

print(f'A média de idade do grupo é de {media_idade} anos.')
print(f'O homem mais velho tem {maior_idade_homem} anos e se chama {nome_velho}.')
print(f'Ao todo são {tot_mulher_20} mulhere(s) com menos de 20 anos.')

# Desafio concluído
