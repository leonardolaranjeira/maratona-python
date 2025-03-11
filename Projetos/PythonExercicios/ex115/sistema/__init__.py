from ex115.sistema.funcs import menu, cores
from os import stat

print(f'{"EXERCÍCIO 115":^70}')

'''Crie um pequeno sistema modularizado que permita cadastrar pessoas pelo seu nome e idade em um arquivo de 
texto simples. O sistema só vai ter 2 opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas.'''

while True:
    try:
        dec = menu(f'{cores(2)}Sua opção: {cores(0)}')

    except KeyboardInterrupt:
        print(f'{cores(1)}\nSistema encerrado pelo usuário.{cores(0)}')

    else:
        if dec == 1:
            if stat('cadastros_ex115.txt').st_size == 0:
                print(f'{cores(1)}Não há nenhuma pessoa cadastrada{cores(0)}')
            else:
                # Listar pessoas
                funcs.listar()

        elif dec == 2:
            # Cadastro
            nome = ""
            idade = ""
            funcs.cadastro(nome, idade)

        elif dec == 3:
            # Sair
            print(f'{cores(1)}Saindo do sistema...{cores(0)}')
            break

# Módulo funções
'''

def cores(cod):
    """
    >> Escolha a cor que deseja usar no texto em específico.
    Cores numeradas (Escolha uma de acordo com a lista)
    0 - Limpa
    1 - Vermelho
    2 - Amarela
    3 - Verde
    """
    cor = ['\033[m', '\033[1;31m', '\033[1;33m', '\033[1;32m']
    return cor[cod]


def menu(msg):
    while True:
        print('-' * 70)
        print(f'{"MENU PRINCIPAL":^70}')
        print('-' * 70)
        print(f'{cores(2)}1 - {cores(3)}Ver pessoas cadastradas.')
        print(f'{cores(2)}2 - {cores(3)}Cadastrar nova pessoa.')
        print(f'{cores(2)}3 - {cores(3)}Sair do sistema.{cores(0)}')
        print('-' * 70)

        decisao = 0
        opc = input(msg).strip()
        # Verificação de inteiro
        if opc.isnumeric():
            decisao = int(opc)

        # Tratamento de erro
        try:
            if 1 <= decisao <= 3:
                return decisao
        except (ValueError, TypeError):
            print(f'{cores(1)}Erro! Este valor não é válido como decisão.{cores(0)}')

        except KeyboardInterrupt:
            print(f'\n{cores(1)}O usuário preferiu encerrar o programa...{cores(0)}')
            return 3
        else:
            return decisao


def cadastro(nome, idade):
    with open('cadastros_ex115.txt', 'a') as arquivo:
        while True:
            global continuar
            try:
                print('-' * 70)
                print(f'{"NOVO CADASTRO":^70}')
                print('-' * 70)
                nome = str(input('Nome: ')).strip()
                idade = str(input('Idade: ')).strip()
                dados = input(f'Estão corretos os dados de \"{nome}\" com \"{idade}\" anos [S/N]? ').strip()
                if dados in 'Ss':
                    if idade.isnumeric() and nome.replace(' ', '').isalpha():
                        arquivo.write(f'{nome}\t\t\t{idade}\n')
                        print(f'{cores(3)}Cadastro realizado com sucesso!{cores(0)}')
                        break
                    else:
                        print(f'{cores(1)}Erro: "NOME" aceita apenas letras e "IDADE" apenas números.{cores(0)}')

                elif dados in 'Nn':
                    print(f'{cores(2)}Por favor, insira novamente os dados.{cores(0)}')
                else:
                    print(f'{cores(1)}Opção inválida, digite apenas "S" para sim ou "N" para não.{cores(0)}')

            except KeyboardInterrupt:
                print(f'{cores(2)}\nCadastro interrompido pelo usuário.{cores(0)}')
                continuar = False  # Encerra o loop principal
                break


def listar():
    try:
        with open('cadastros_ex115.txt', 'r') as arquivo:
            print('-' * 70)
            print(f"{'PESSOAS CADASTRADAS':^70}")
            print('-' * 70)
            for linha in arquivo:
                nome, idade = linha.strip().split('\t\t\t')
                print(f'{nome:<50}{idade} anos')

    except Exception as erro:
        print(f'Erro: {erro.__cause__}')

'''