from random import randint

print('Exercício 74')

'''Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de 
números gerados e também indique o menor e o maior valor que estão na tupla.'''

decisao = ''
maior = 0
while decisao != 'N':
    decisao = str(input('Deseja gerar novos números? [S/N]\n')).strip().upper()[0]
    if decisao == 'N':
        print('Encerrando programa...')
        break
    if decisao not in ['S', 'N']:
        print('Opção inválida. Tente novamente!')
        print('=-' * 30)
    else:
        n1 = randint(0, 100)
        n2 = randint(0, 100)
        n3 = randint(0, 100)
        n4 = randint(0, 100)
        n5 = randint(0, 100)
        tupla = (n1, n2, n3, n4, n5)

        print('=-' * 30)
        print(f'Estes foram os 5 números gerados:\n{tupla}')
        print(f'Sendo o maior número {max(tupla)} e o menor número {min(tupla)}.')
        print('=-' * 30)

# Desafio concluído!
