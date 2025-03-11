
print('Exercício 69')

'''Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar
se o usuário quer ou não continuar. No final, mostre:
A) Quantas pessoas tem mais de 18 anos.
B) Quantos homens foram cadastrados.
C) Quantas mulheres tem menos de 20 anos.'''


tot18 = totH = totM20 = 0
sexo = ''
while True:
    print('=-' * 20)
    print(f'{'CADASTRO DE PESSOA': ^40}')
    print('=-' * 20)

    nome = str(input('Olá, qual o seu nome?\n>> ')).strip()
    idade = int(input('Qual a sua idade?\n>> '))
    sexo = ' '
    while sexo != 'M' and sexo != 'F':
        sexo = str(input('Qual o seu sexo? [M/F]\n>> ')).strip().upper()[0]
    if sexo not in 'MF':
        print('Opção inválida. Digite novamente o sexo!')

    if idade >= 18:
        tot18 += 1
    # Está parte está dando bug.

    if sexo == 'M':
        totH += 1

    if sexo == 'F' and idade < 20:
        totM20 += 1

    print('=-' * 20)
    decisao = ' '
    while decisao != 'S' and decisao != 'N':
        decisao = str(input('Você quer continuar? [S/N]\n>> ')).strip().upper()[0]
    if decisao == 'N':
        print('Encerrando programa...')
        break
    elif decisao not in 'SN':
        print('Opção inválida, Tente novamente.')

print(f'Total de pessoas com mais de 18 anos: {tot18}.')
print(f'Ao todo temos {totH} homens cadastrados.')
print(f'E temos {totM20} mulher(es) com menos de 20 anos.')

# Desafio concluído!
