
print('Exercício 37')

'''Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a 
"base de conversão". 1)Para binário, 2)Para octal ou 3)Para hexadecimal'''


num = int(input('Digite um número inteiro qualquer: '))
print('Qual base de conversão você gostaria de usar no seu número escolhido? ')
base = int(input('1) Para binário\n'
                 '2) Para octal\n'
                 '3) Para Hexadecimal\n'
                 'Digite aqui sua escolha: '))

binario = bin(num)[2:]
octal = oct(num)[2:]
hexadecimal = hex(num)[2:]

if base == 1:
    print('O número {} em binário fica {}.'.format(num, binario))
elif base == 2:
    print('O número {} em octal fica {}'.format(num, octal))
elif base == 3:
    print('O número {} em hexadecimal fica {}'.format(num, hexadecimal))
else:
    print('Opção inválida, tente novamente!')

# Desafio concluído!
