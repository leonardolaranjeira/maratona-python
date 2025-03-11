print('Exercício 15')

# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos
# quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input('Qual a quantidade de quilômetros percorridos pelo carro alugado? '))
dias = int(input('Qual a quantidade de dias que foi alugado? '))

calc = (km*0.15)+(dias*60)

print('O carro percorreu {} kms em {} dias!'.format(km, dias))
print('...')
print('Sabendo disso, este carro soma um total de R${:.2f} em custos, sendo R${:.2f} de Kms percorridos e R${:.2f} de '
      'dias de uso!'.format(calc, km*0.15, dias*60))

# Desafio concluído!
