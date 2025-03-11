print('Exercício 13')

# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

sal = float(input('Qual o salário do funcionário: R$'))
novo = sal + (sal*15/100)

print('O salário deste funcionário foi de R${:.2f}, com 15% de aumento, passa a receber R${:.2f}!'.format(sal, novo))

# Desafio concluído!
