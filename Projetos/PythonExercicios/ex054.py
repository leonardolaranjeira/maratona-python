from datetime import date
print('Exercício 54')

'''Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram
a maioridade e quantas já são maiores. (Considere a maior idade com 21 anos)'''

ano_atual = date.today().year

total_maior = 0
total_menor = 0
for ps in range(1, 8):
    ano_nasc = int(input(f'Em que ano a {ps}ª pessoa nasceu? '))
    idade = ano_atual - ano_nasc
    if idade >= 21:
        total_maior += 1
    else:
        total_menor += 1
print(f'Ao todo tivemos {total_maior} pessoas maiores de idade.')
print(f'E também tivemos {total_menor} pessoas menores de idade.')

# Desafio concluído
