def moeda(num):
    mone = f'R$ {num:.2f}'
    return mone


def aumentar(num, real=False):
    if real:
        aum = f'R$ {num + (0.10 * num):.2f}'
    else:
        aum = num + (0.10 * num)
    return aum


def diminuir(num, real=False):
    if real:
        dim = f' R$ {num - (0.13 * num):.2f}'
    else:
        dim = num - (0.13 * num)
    return dim


def dobro(num, real=False):
    if real:
        dob = f' R$ {(num * 2):.2f}'
    else:
        dob = num * 2
    return dob


def metade(num, real=False):
    if real:
        met = f' R$ {(num / 2):.2f}'
    else:
        met = num / 2
    return met