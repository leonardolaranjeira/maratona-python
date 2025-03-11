
print('Exercício 105')

'''Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário
com as seguintes informações:
- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)

Adcione também as docstrings da função'''

def notas(*num):
    """
    > Pega todas as notas obtidas pelo usuário e transforma em informações.
    :param num: valores obtidos pela entrada de dados.
    """
    media = sum(alunos['notas']) / len(alunos['notas'])
    resultado = ("Aprovado" if media >= 7 else "Recuperação" if nota >= 5 else "Reprovado")
    print(f' - Quantidade de notas: {len(alunos['notas'])}'
          f'\n - A maior nota: {max(alunos['notas'])}'
          f'\n - A menor nota: {min(alunos['notas'])}'
          f'\n - A média da turma: {media:.2f}'
          f'\n - Situação: {resultado}')


cont = 0
media_aluno = []
alunos = {}

while True:
    cont += 1
    print('-=' * 20)
    nota = float(input(f'Digite a {cont}ª nota: '))
    media_aluno.append(nota)

    decisao = str(input('Quer continuar [S/N]? ')).strip()[0]
    if decisao in 'Nn':
        alunos['notas'] = media_aluno.copy()
        break

print('-=' * 20)
print(alunos['notas'])
notas(alunos['notas'])

print()
print('Encerrando programa...')

# Desafio concluído!
