from datetime import datetime
print('Exercício 39')

''' Faça um programa que leia o ano de nascimento de um jovem e informe , de acordo com sua idade:

- Se ele ainda vai se alistar ao serviço militar.
- Se é a hora de se alistar.
- Se já passou do tempo do alistamento.

    Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''

print('Verificador de alistamento!')

nasc = int(input('Digite o ano em que nasceu: '))
ano_atual = datetime.now().year
idade = ano_atual - nasc
tempo = idade - 18

if idade == 18:
    print('Já está na hora de se alistar, busque um quartel o quanto antes!')
elif idade < 18:
    print('Ainda não deu a hora de se alistar, falta {} ano(s) para o alistamento!'.format(abs(tempo)))
else:
    print('Já foi se alistar? Se não, já se passou {} ano(s) desde a sua data de alistamento!'.format(abs(tempo)))

# Desafio concluído!
