print('Exercício 22')

''' Crie um programa que leia o nome completo de uma pessoa e mostre: 
- O nome com todas as letras maiúsculas
- O nome com todas as letras minúsculas
- Quantas letras ao todo (Sem considerar espaços)
- Quantas letras tem o primeiro nome.'''

nome = str(input('Digite seu nome: ')).strip()

print('Todas as letras maiúsculas: {}'.format(nome.upper()))
print('Todas as letras minúsculas: {}'.format(nome.lower()))
print('Contagem de carácteres é igual à: {}'.format(len(nome) - nome.count(' ')))
# print('No primeiro nome há: {} letras.'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras.'.format(separa[0], len(separa[0])))

# Desafio concluído!
