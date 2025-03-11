print('Exercício 13 - Extra')

# Faça um algoritmo que leia o preço de um produto e mostre o valor dele com desconto de 10% à vista,
# e com aumento de 8% a prazo.

preco = float(input('Qual o preço do produto: R$'))
vista = preco - (preco*10/100)
prazo = preco + (preco*8/100)

print('O valor deste produto à vista fica por R${:.2f} com 10% de desconto, e sendo pago a prazo o valor '
      'fica por R${:.2f} com 8% de aumento no valor.'.format(vista, prazo))

# Desafio concluído!
