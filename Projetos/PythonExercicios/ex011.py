print('Exercício 11')

# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta
# necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².

print('Calcula a área da sua parede!')

largura = float(input('Largura - Digite um valor: '))
altura = float(input('Altura - Digite um valor: '))

area = largura*altura

print('Sua parede tem a área de {}m²!'.format(area))
print('...')

tinta = area/2

print('A tinta escolhida pinta 2m² por litro, sendo assim, você vai precisar de uma média de\n{:.2f} litros '
      'de tinta para pintar sua parede!'.format(tinta))

# Desafio concluído!
