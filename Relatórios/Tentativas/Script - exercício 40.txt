bold = '\033[1m'
vermelha_N = '\033[1:31m'
vermelha = '\033[0:31m'
azul = '\033[0:34m'
verde_N = '\033[1:32m'
limpa = '\033[m'

print('{}Exercício 40{}'.format(verde_N, limpa))

'''Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo 
com a média atingida:
    - Média abaixo de 5.0: REPROVADO
    - Média entre 5.0 e 6.9: RECUPERAÇÃO
    - Média 7.0 ou superior: APROVADO'''

n1 = float(input('{}Digite a primeira nota:{} '.format(bold, limpa)))
n2 = float(input('{}Digite a segunda nota:{} '.format(bold, limpa)))
media = (n1 + n2) / 2

if media < 5.0:
    print('Com {} e {} a média do aluno é {}'.format(n1, n2, media))
    print('{}REPROVADO!{}\n{}Estude mais...{}'.format(vermelha_N, limpa, azul, limpa))

elif media == 5.0 or media <= 6.9:
    print('Com {} e {} a média do aluno é {}'.format(n1, n2, media))
    print('{}RECUPERAÇÃO!{}\n{}Estude mais...{}'.format(vermelha, limpa, azul, limpa))

else:
    print('Com {} e {} a média do aluno é {}'.format(n1, n2, media))
    print('{}APROVADO!{}\n{}Parabéns!!!\nContinue estudando.{}'.format(verde_N, limpa, azul, limpa))

# Desafio concluído!
