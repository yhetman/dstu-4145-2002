
from random import randint
from consts import *

def power(x, k):
    prod = 1
    while k > 0:
        if k & 1 == 1:
            prod = multiplication(x, prod)
        x = multiplication(x, x)
        k = k >> 1
    return prod


def inverse(x):
    k = (1 << m) - 2 # заменить на константу!
    return power(x, k)



def division(x, y):
    return multiplication(x, inverse(y))



def multiplication(x, y):
    mult = 0

    while x and y:
        if y & 1 == 1:
            mult ^= x
        y >>= 1
        temp = x >> (m - 1)
        x = (x << 1) & prim_eleme
        if temp == 1:
            x ^= prim_eleme & polinominal
    return mult


