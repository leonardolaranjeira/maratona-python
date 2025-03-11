
VERMELHO = '\033[1:31m'
VERDE = '\033[1:33m'
LIMPA = '\033[m'

print('Exercício 90')
print('-=' * 30)

'''Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, 
mostre o conteúdo da estrutura na tela'''

alunos = {'nome': str(input('Digite o nome do aluno: ')),
          'media': float(input('Digite a média do aluno: '))}

print('-=' * 30)
while True:
    print(f'Nome do aluno: {alunos["nome"]}')
    print(f'A média de {alunos["nome"]} é: {alunos["media"]}')
    if 0 < alunos['media'] < 11:
        if alunos['media'] <= 6.9:
            print(f'Situação: {VERMELHO}REPROVADO{LIMPA}')
            break
        elif alunos['media'] >= 7:
            print(f'Situação: {VERDE}APROVADO{LIMPA}')
            break
    else:
        print('-=' * 30)
        print(f'{VERMELHO}Valor inválido, encerrando programa...{LIMPA}')
        break

# Desafio concluído!
