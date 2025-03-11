
B_cinza_preto = '\033[7;30;47m'
B_Preto_branco = '\033[1;30;47m'
B_Branco_vermelho = '\033[1;30;41m'
limpa = '\033[m'

print('Exercício 106')

'''Faça um mini sistema que utilize o interactive Help do Python. O usuário vai digitar o comando e o manual vai 
aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará.

OBS: use cores.'''
def ajuda():
    while True:
        print(f"{limpa}{'--' * 35}")
        pesquisa = str(input('Função ou biblioteca ["fim": encerra] > ')).strip()
        print('--' * 35)
        if pesquisa != 'fim':
            print(f"{B_cinza_preto}{'-=' * 35}\nAcessando o manual do comando '{pesquisa}'\n{'-=' * 35}")

            print(B_Preto_branco)
            help(pesquisa)

        elif pesquisa in 'fim':
            print(f"{B_Branco_vermelho}{'-=' * 35}\n{'Até logo':^50}\n{'-=' * 35}\n{limpa}")
            break


ajuda()

# Desafio concluído
