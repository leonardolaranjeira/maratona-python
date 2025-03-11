from time import sleep
print('Exercício 89')

'''Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. 
No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar 
as notas de cada aluno individualmente.'''

pessoa = []
medias = []

while True:
    pessoa.append(str(input('Digite seu nome: ')))
    n1 = float(input('1ª Nota: '))
    n2 = float(input('2ª Nota: '))
    pessoa.append([n1, n2, (n1 + n2) / 2])
    medias.append(pessoa[:])
    pessoa.clear()

    decisao = str(input('Quer continuar [S/N]? ')).upper().strip()[0]
    if decisao == 'N':
        print('=-' * 30)
        break

print(f'{'N°':<3}{'NOME':<10}{'N1':<10}{'N2':<10}{'MÉDIA'}')
print('--' * 30)

for cod in range(0, len(medias)):
    print(f'{cod:<3}{medias[cod][0]:<10}{medias[cod][1][0]:<10}{medias[cod][1][1]:<10}{medias[cod][1][2]}')
print('--' * 30)

while True:
    notas = int(input('Mostrar notas de qual aluno (999 interrompe)? '))
    if notas == 999:
        print('FINALIZANDO...')
        sleep(1)
        break
    elif notas <= len(medias) - 1:
        print(f'Notas de {medias[notas][0]} são: {medias[notas][1][0]} e {medias[notas][1][1]}')
        print('--' * 30)

print(f'{'<<< VOLTE SEMPRE! >>>':^30}')

# Desafio concluído!
