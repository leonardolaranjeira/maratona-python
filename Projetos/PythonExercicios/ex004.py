print('Exercício 4 - Especificando informações e tipos primitivos!')

palavra = input('Digite uma palavra usando números, letras ou os dois: ')
print('Esta variável está definida como um tipo:', type(palavra))
print('A palavra {} contêm apenas números? '.format(palavra), palavra.isnumeric())
print('A palavra {} contêm apenas letras? '.format(palavra), palavra.isalpha())
print('A palavra {} está escrito apenas em letras maiúsculas? '.format(palavra), palavra.isupper())
print('A palavra {} está escrito apenas em letras minúsculas? '.format(palavra), palavra.islower())
print('Está palavra esta definida como alpha numérico? ', palavra.isalnum())

# Desafio concluído!
