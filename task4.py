#!/usr/bin/env python


def primefactors(x):
    factorlist = []
    loop = 2
    while loop <= x:
        if x % loop == 0:
            x /= loop
            factorlist.append(loop)
        else:
            loop += 1
    return factorlist


def is_prime(a):
    return all(a % i for i in range(2, a))


n = int(input())
if is_prime(n):
    print('-1')
else:
    print(''.join(list(map(str, sorted(primefactors(n))))))
