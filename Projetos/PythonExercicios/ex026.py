print('Exercício 26')

'''Faça um programa que leia uma frase pelo teclado e mostre:
- Quantas vezes aparece a letra "A".
- Em que posição ela aparece a primeira vez.
- Em que posição ela aparece a última vez.'''

frase = str(input('Digite uma frase: ')).strip().upper()

print('"{}" contém {} caracteres.'.format(frase, len(frase)))

print('Há {} letras "a" na frase.'.format(frase.count('A')))

print('Sua primeira letra "a" está no caracter {} da frase.'.format(frase.find('A')+1))

print('Seu último "a", está na posição {}.'.format(frase.rfind('A')+1))

# Desafio concluído!
