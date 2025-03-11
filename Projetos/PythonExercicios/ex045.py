from random import choice

vermelhoB = '\033[1:31m'
verdeB = '\033[1:32m'
amareloB = '\033[1:33m'
Fpreto_vermelhoB = '\033[1:31:40m'
Fpreto_verdeB = '\033[1:32:40m'
Fcinza_verdeB = '\033[1:32:40m'
limpa = '\033[m'

print(f'{verdeB}Exercício 45{limpa}')

'''Crie um programa que faça o computador jogar jokenpô com você.'''

print(f'{Fpreto_verdeB}Pedra, papel ou tesoura?{limpa}')

jokempo = ['Pedra', 'Papel', 'Tesoura']

pc = choice(jokempo)

print(f'{Fpreto_verdeB}JOKEMPO!!!{limpa}\n{vermelhoB}PEDRA{limpa}\n{verdeB}PAPEL{limpa}\n{amareloB}TESOURA{limpa}')

pessoa = str(input('Digite a sua escolha: ')).strip().capitalize()
print('Computador:', pc)
print('Pessoa:', pessoa)

if pessoa == pc:
    print('{}EMPATE!!!{}\nAmbos escolheram {}.'.format(Fpreto_vermelhoB, limpa, pc))

elif (pessoa == 'Pedra' and pc == 'Tesoura' or pessoa == 'Papel' and pc == 'Pedra'
      or pessoa == 'Tesoura' and pc == 'Papel'):
    print('{}VOCÊ GANHOU!!!{}\nO computador escolheu {}, você escolheu {}.'
          .format(Fcinza_verdeB, limpa, pc, pessoa))

elif (pc == 'Pedra' and pessoa == 'Tesoura' or pc == 'Papel' and pessoa == 'Pedra'
      or pc == 'Tesoura' and pessoa == 'Papel'):
    print('{}COMPUTADOR GANHOU!!!{}\nO computador escolheu {} e você escolheu {}.'
          .format(Fpreto_vermelhoB, limpa, pc, pessoa))

else:
    print('Esta não é uma das opções entre "Pedra, Papel ou Tesoura"')

# Desafio concluído!
