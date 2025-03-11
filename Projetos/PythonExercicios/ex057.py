
print('Exercício 57')

'''Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a
digitação novamente até ter um valor correto.'''

sexo = ''
while sexo != 'M' and sexo != 'F':
    nome = str(input('Qual o seu nome? '))
    sexo = str(input('Qual o seu sexo? [M/F] ')).upper()
    if sexo == 'M' or sexo == 'F':
        print(f'Obrigado pela participação, {nome}!')
    else:
        print('O sexo digitado não é uma das opções, tente novamente!')

# Desafio concluído!
