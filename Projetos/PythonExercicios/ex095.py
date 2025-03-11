print('Exercicio 95')

'''Aprimore o DESAFIO 093 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes
 do aproveitamento de cada jogador.'''

time = list()
jogador = dict()
partidas = list()

while True:
    # Coleta de dados dos jogadores.
    nome = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas {nome} jogou? '))
    print('-=' * 50)
    for c in range(0, tot):
        partidas.append(int(input(f'Quantos gols na partida {c + 1}? ')))
    jogador['nome'] = nome
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)

    time.append(jogador.copy())
    partidas.clear()
    jogador.clear()

    while True:
        print('-=' * 50)
        decisao = str(input('Quer continuar [S/N]? ')).upper()[0]
        if decisao in 'SN':
            break
        print('Decisão incorreta, digite novamente.')
    if decisao in 'N':
        break

while True:
    print('-=' * 40)
    print(f'{'Cód':<5}{f'Nome':<15}{f'Gols':<30}{f'Total':<10}')
    print('-=' * 40)
    for p, j in enumerate(time):
        print(f'{p:<5}{j["nome"]:<15}{str(j["gols"]):<30}{j["total"]:<10}')
    print('-=' * 40)

    resp = int(input('Mostrar dados de qual jogador (999 para encerrar)? '))
    if resp == 999:
        print('-=' * 30)
        print('<<< ENCERRANDO PROGRAMA >>>')
        break
    if resp >= len(time):
        print(f'Erro: Não existe jogador com código {resp}.')
    else:
        while True:
            if 0 <= resp <= len(time):
                print('-=' * 30)
                j = time[resp]
                print(f'Levantamento do jogador: {j["nome"]}')
                print(f'Partidas jogadas: {len(j["gols"])}')
                print(f'Gols: {j["gols"]}')
                print(f'Total de gols: {j["total"]}')
                break
            else:
                print('-=' * 30)
                print('Valor inválido!')
                break

    # Desafio concluído!
