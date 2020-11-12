#!/usr/bin/env python3
# -*- config: utf-8 -*-

# Вариант 3.
# Ввести список А из 10 элементов, найти наименьший элемент и переставить его с
# последним элементом. Преобразованный массив вывести.

import sys

if __name__ == '__main__':
    a = tuple(map(int, input().split()))
    if len(a)!= 10:
        print('Недопустимый размер кортежа', file=sys.stderr)
        exit(1)

    b = list(a)
    i_min = b.index(min(b))
    b[0], b[i_min] = b[i_min], b[0]
    a = tuple(b)
    print(a)