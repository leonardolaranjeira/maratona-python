from requests import get

cores= {'Vermelho':'\033[1:31m', 'Amarelo':'\033[1:33m', 'Limpa':'\033[m'}

print('Exercício 114')

'''Crie um código em Python que teste se o site pudim está acessível pelo computador usado.'''


url = "https://www.youtube.com/watch?v=VnfZyFI8iek"
url1 = 'http://www.pudim.com.br'

try:
    if get(url).status_code == 200:
        print(f'{cores["Amarelo"]}Consegui acessar o  vídeo do "Você sabia" com sucesso!{cores["Limpa"]}')
except ConnectionError:
    print(f'{cores["Vermelho"]}O vídeo do "você sabia" não está acessível no momento.{cores["Limpa"]}')
except Exception as erro:
    print(f'{cores["Amarelo"]}O erro encontrado foi:{cores["Limpa"]} {erro.__cause__}')

# Desafio concluído!
