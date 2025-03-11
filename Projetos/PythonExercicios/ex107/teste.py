import moeda

print('Exercício 107')

'''Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
Faça também um programa que importe esse módulo e use algumas dessas funções.'''

p = float(input('Digite o preço: R$ '))
print(f'A metade de {p} é: {moeda.metade(p)}')
print(f'O dobro de {p} é: {moeda.dobro(p)}')
print(f'aumentando 10% temos: {moeda.aumentar(p)}')
print(f'Reduzindo 13% temos: {moeda.diminuir(p)}')