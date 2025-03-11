
print('Exercício 84')

'''Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No finals mostre:
    A) Quantas pessoas foram cadastradas.
    B) Uma listagem com as pessoas mais pesadas.
    C) Uma listagem com as pessoas mais leves'''

dados = []
pessoas = []
peso_menor = []
peso_maior = []

while True:
    dados.append(str(input('Digite seu nome: ')))
    dados.append(float(input('Digite seu peso: ')))

    if len(peso_menor) == 0 or dados[1] < peso_menor[0]:
        peso_menor = [dados[1]]

    if len(peso_maior) == 0 or dados[1] > peso_maior[0]:
        peso_maior = [dados[1]]

    pessoas.append(dados[:])
    dados.clear()

    decisao = str(input('Deseja continuar [S/N]? ')).strip().upper()[0]
    if decisao in 'N':
        break

print('-=' * 30)
print(f'Foram cadastradas {len(pessoas)} pessoas no total.')
print(f'O maior peso foi de {peso_maior[0]:.2f}Kgs, sendo o peso de: ', end='')
print(', '.join([x[0] for x in pessoas if x[1] == peso_maior[0]]))
print(f'O menor peso foi de {peso_menor[0]:.2f}Kgs, sendo o peso de: ', end='')
print(', '.join([x[0] for x in pessoas if x[1] == peso_menor[0]]))

# Desafio concluído!
