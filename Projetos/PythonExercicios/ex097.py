
print('Exercício 97')

'''Faça um programa que tenha a função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma
 mensagem com tamanho adaptável.
 
 Ex: escreva('Olá, mundo!')
 
 Saída:
 ------------
  Olá mundo!
 ------------'''


msg = str(input('Digite uma mensagem: '))


def escreva(msg):
    print('-' * (len(msg) + 2))
    print(f'{msg:^{len(msg) + 2}}')
    print('-' * (len(msg) + 2))


escreva(msg)

# Desafio concluído!
