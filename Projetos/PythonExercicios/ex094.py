print('Exercício 94')

'''Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário 
e todos os dicionários em uma lista. No final, mostre:
    A) Quantas pessoas foram cadastradas
    B) A média de idade do grupo.
    C) uma lista com todas as mulheres.
    D) Uma lista com todas as pessoas com idade acima da média'''

cont = tot_idade = media_idade = 0
pessoas = {}
pessoa = []
mulheres = []
acima = []

while True:
    nome = str(input('Qual o seu nome? '))
    sexo = str(input('Qual o seu sexo? [M/F]: ')).strip().upper()[0]
    idade = int(input('Qual a sua idade? '))
    pessoa = [nome, sexo, idade]
    pessoas[nome] = pessoa.copy()
    cont += 1
    tot_idade += idade

    if sexo in ['F']:
        mulheres.append(nome)

    decisao = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    print('-=' * 30)

    if decisao in ['N']:
        pessoas["mulheres"] = mulheres
        if cont > 0:
            media_idade = tot_idade / cont

        print(f'No dicionário tem: ')
        print(pessoas)
        print(f'> O grupo tem {cont} pessoas.')
        print(f'> A média de idade é de {media_idade:.2f} anos.')
        print(f'> As mulheres cadastradas foram: {pessoas["mulheres"]}')
        print(f'LISTA DAS PESSOAS QUE ESTÃO ACIMA DA MÉDIA:')
        for nome in pessoas:
            if len(pessoas[nome]) > 2 and pessoas[nome][2] > media_idade:
                acima.append(pessoas[nome][0])
        print(acima)
        break

# Desafio concluído!
