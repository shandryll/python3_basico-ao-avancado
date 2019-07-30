# -*- coding: utf-8 -*-
import math
import sys


def circulo(raio):
    return math.pi * (raio ** 2)


def help():
    print('É necessário informar o raio do círculo.\nSintaxe: {sys.argv[0][-7:]} <raio>')


if __name__ == '__main__':
    if len(sys.argv) < 2:
        help()
        sys.exit(1)
    else:
        raio = float(input('Digite o raio da circunferência: '))
        area = circulo(raio)
        print('Área do círculo:', area)
