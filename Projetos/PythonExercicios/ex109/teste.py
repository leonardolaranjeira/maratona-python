import moeda

print('Exercício 109')

'''Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o 
valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desadio 108.'''

p = float(input('Digite o preço: R$ '))
print(f'A metade de {moeda.moeda(p)} é: {moeda.metade(p, True)}')
print(f'O dobro de {moeda.moeda(p)} é: {moeda.dobro(p, False)}')
print(f'aumentando 10% temos: {moeda.aumentar(p, True)}')
print(f'Reduzindo 13% temos: {moeda.diminuir(p, True)}')

# Desafio concluído!
