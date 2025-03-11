
cores= {'Vermelho':'\033[1:31m', 'Amarelo':'\033[1:33m', 'Limpa':'\033[m'}

print('Exercício 113')

'''Reescreva a função leiaint() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número 
de tipo inválido. Aproveite e crie também uma função leiafloat() com a mesma funcionalidade.'''

def leiaint(msg):
    ok = False
    inteiro = 0
    while True:
        try:
            i = str(input(msg)).strip()
            if i.isnumeric():
                inteiro = int(i)
                ok = True
                break
            else:
                print(f'{cores['Vermelho']}Erro! Este valor não é válido como inteiro.{cores['Limpa']}')

        except KeyboardInterrupt:
            print(f'{cores['Vermelho']}O usuário preferiu não digitar nenhum inteiro.{cores['Limpa']}')
            return 0
        except Exception as erro:
            print(f'{cores['Amarelo']}O erro encontrado foi:{cores['Limpa']} {erro.__cause__}')

    return inteiro


def leiafloat(msg):
    ok = False
    real = 0.0
    while True:
        try:
            f = str(input(msg)).strip().replace(',', '.')
            real = float(f)
            ok = True
            break

        except (ValueError, TypeError):
            print(f'{cores['Vermelho']}Erro! O valor digitado não é um valor real.{cores['Limpa']}')
            continue
        except KeyboardInterrupt:
            print(f'{cores['Vermelho']}O usuário preferiu não digitar nenhum valor real.{cores['Limpa']}')
            return 0.0

        except Exception as erro:
            print(f'{cores['Amarelo']}O erro encontrado foi:{cores['Limpa']} {erro.__cause__}')

    return real


# Programa principal!
i = leiaint('Digite um número inteiro: ')
f = leiafloat('Digite um valor real: ')

print('-' * 50)
print(f'O valor inteiro digitado foi: {i}')
print(f'O valor real digitado foi: {f}')
print('-' * 50)

# Desafio corrigído!
