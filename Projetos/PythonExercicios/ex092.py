from datetime import datetime

print('Exercício 92')

'''Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os(com idade) em um dicionário 
se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e 
acrescente, além da idade, com quantos anos a pessoa vai se aposentar.'''

ano_atual = datetime.now().year

Dados = {'nome': str(input('Qual o seu nome? ')),
         'nasc': int(input('Qual o ano de nascimento? ')),
         'ctps': str(input('Possui carteira de trabalho? (Digite 0 se não tem) ')),
         'contratacao': int(input('Ano de contratação: ')),
         'salario': float(input('Qual o salário? '))}

if Dados['ctps'] == '0':
    print('-=' * 30)
    print(f'Nome tem o valor: {Dados["nome"]}')
    print(f'Idade tem o valor: {ano_atual - Dados["nasc"]}')
    print(f'CTPS tem o valor: {'Você não possui carteira de trabalho.'}')
else:
    print('-=' * 30)
    print(f'Nome tem o valor: {Dados["nome"]}')
    print(f'Idade tem o valor: {ano_atual - Dados["nasc"]}')
    print(f'CTPS tem o valor: {Dados["ctps"]}')
    print(f'Contratação tem o valor: {Dados["contratacao"]}')
    print(f'Salário tem o valor: {Dados["salario"]}')
    print(f'Aposentadoria será concluída com a idade: {(ano_atual - Dados["contratacao"]) + 35}')

# Desafio concluído!
