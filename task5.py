#!/usr/bin/env python


matrix = []
n = int(input('input matrix size: '))
matrix.append(n)
for i in range(n):
    matrix.append(list(map(int, input(f'{i+1} line:').split())))


def diagonal(n):
    size = n[0]
    matrix = n[1:]
    dia1 = 0
    dia2 = 0
    for i in range(size):
        dia1 += matrix[0+i][0+i]
        dia2 += matrix[0+i][-1-i]
    return abs(dia1-dia2)


print(diagonal(matrix))
