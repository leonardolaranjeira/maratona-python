print('Exercício 8 - Extra')

# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

print('Medidas de comprimentos em Quilômetros, Hectômetros, Decâmetros, metros, Decimetros, centímetro e milímetros! \n')

metros = float(input('Digite um valor em metros: '))
print('O valor definido em metros foi: {:.1f} \n'.format(metros))

km = metros/1000
print('{} mtr em quilômetros é igual à: {} km'.format(metros, km))

hm = metros/100
print('{} mtr em hectômetros é igual à: {} hm'.format(metros, hm))

dam = metros/10
print('{} mtr em decâmetros é igual à: {} dam'.format(metros, dam))

print('O valor em mêtros é {}!'.format(metros))

dm = metros*10
print('{} mtr em decimetros é igual à: {:.0f} dm'.format(metros, dm))

cm = metros*100
print('{} mtr em centímetros é igual à: {:.0f} cm'.format(metros, cm))

mm = metros*1000
print('{} mtr em milímetros é igual à: {:.0f} mm'.format(metros, mm))

# Desafio concluído!
