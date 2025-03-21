
print('Exercício 73')

'''Crie uma tupla preenchida com os 20 primeiros colocados da tabela do campeonato brasileiro de futebol, na ordem de
 colocação. Depois mostre:
    A) Apenas os 5 primeiros colocados.
    B) Os últimos 4 colocados da tabela.
    C) Uma lista com os times em ordem alfabética.
    D) Em que posição na tabela está o time da criciúma.'''

camp = ('Botafogo', 'Palmeiras', 'Flamengo', 'Bahia', 'Cruzeiro', 'São Paulo', 'Fortaleza', 'Athletico-PR',
        'Red bull bragantino', 'Atlético-MG', 'Vasco', 'Internacional', 'Juventude', 'Criciúma', 'Cuiabá', 'Vitória',
        'Corinthians', 'Grêmio', 'Atlético-GO', 'Fluminense')

print(f'A) Os 5 primeiros times da lista são: {camp[0:5]}')
print(f'B) Os últimos 4 colocados são: {camp[16:]}')
print(f'C) Organizados em ordem alfabética: {sorted(camp)}')
print(f'D) O time do criciúma está na posição {camp.index('Criciúma') + 1}')

# Desafio concluído!
