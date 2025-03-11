
print('Exercício 31')

'''Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50
por Km para viagens de até 200Km e R$0,45 para viagens mais longas.'''

viagem = int(input('Qual a distância da sua viagem em Kms: '))

if viagem <= 200:
    print('O valor de sua viagem fica no valor de R${}'.format(viagem * 0.50))
else:
    print('O valor de sua viagem fica no valor de R${}'.format(viagem * 0.45))

# Desafio concluído!
