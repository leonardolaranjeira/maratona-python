
print('Exercício 38')

'''Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
"O primeiro valor é maior", "O segundo valor é maior" ou "Não existe valor maior, os dois são iguais"'''

print('Digite dois números e compare qual deles é maior!')
n1 = float(input('Digite o primeiro valor: '))
n2 = float(input('Digite o segundo valor: '))

if n1 > n2:
    print('{} é maior que {}, por tanto, o primeiro valor é maior que o segundo valor!'.format(n1, n2))
elif n2 > n1:
    print('{} é maior que {}, por tanto, o segundo valor é maior que o primeiro valor!'.format(n2, n1))
else:
    print('Não existe valor maior, os dois são iguais!')

# Desafio concluído!
