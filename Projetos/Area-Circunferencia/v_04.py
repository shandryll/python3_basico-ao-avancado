# -*- coding: utf-8 -*-
import math
import sys


class TerminalColor:
    text_red = '\033[91m'
    text_white = '\033[0m'

def circulo(raio):
    return math.pi * (raio ** 2)


def help():
    print(TerminalColor.text_red + 'É necessário informar o raio do círculo.\n'
                                   f'Sintaxe: {sys.argv[0][-7:]} <raio>' + TerminalColor.text_white)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        help()
        sys.exit(1)
    else:
        raio = float(input('Digite o raio da circunferência: '))
        area = circulo(raio)
        print('Área do círculo:', area)
