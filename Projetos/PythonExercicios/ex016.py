from math import trunc
print('Exercício 16')

# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.
# Ex: "Digite um número: 6.127", "O número 6.127 tem a parte inteira 6."

print('Arredonde um valor real!')

valor = float(input('Digite um valor: '))
print('O número {} tem a parte inteira {}'.format(valor, trunc(valor)))

# Versão do script sem usar função!

'''valor = float(input('Digite um valor: '))
print('O número {} tem a parte inteira {}'.format(valor, int(valor)))'''

# Desafio concluído!
