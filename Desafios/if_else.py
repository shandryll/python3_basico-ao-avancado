# -*- coding: utf=8 -*-

def exibir_conceito(conceito):
    if conceito == 'err':
        print(f'A nota informada é inválida')
    else:
        print(f'O aluno obteve o conceito final de {conceito}, baseado na nota informada.')


def verificar_nota(nota):
    if 9.1 < nota <= 10:
        conceito = 'A'
        exibir_conceito(conceito)

    elif 8.1 < nota <= 9:
        conceito = 'A-'
        exibir_conceito(conceito)

    elif 7.1 < nota <= 8:
        conceito = 'B'
        exibir_conceito(conceito)

    elif 6.1 < nota <= 7:
        conceito = 'B-'
        exibir_conceito(conceito)

    elif 5.1 < nota <= 6:
        conceito = 'C'
        exibir_conceito(conceito)

    elif 4.1 < nota <= 5:
        conceito = 'C-'
        exibir_conceito(conceito)

    elif 3.1 < nota <= 4:
        conceito = 'D'
        exibir_conceito(conceito)

    elif 2.1 < nota <= 3:
        conceito = 'D-'
        exibir_conceito(conceito)

    elif 1.1 < nota <= 2:
        conceito = 'E'
        exibir_conceito(conceito)

    elif 0 < nota <= 1:
        conceito = 'E-'
        exibir_conceito(conceito)

    else:
        conceito = 'err'
        exibir_conceito(conceito)


if __name__ == '__main__':
    try:
        nota = float(input('Digite o valor da nota: '))
        verificar_nota(nota)

    except ValueError as err_value:
        print(f'A nota informada é inválida')
