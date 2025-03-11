print('Exercício 27')

'''Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o 
último nome separadamente.

Ex: Ana Maria de Souza
primeiro = Ana
Último = Souza'''

nom = str(input('Digite um nome completo: ')).strip()
nome = nom.split()

print('Analisando o nome "{}"...'.format(nom))

print('O primeiro nome é: {}'.format(nome[0]))

print('O último nome é: {}'.format(nome[len(nome)-1]))

# Desafio concluído!
