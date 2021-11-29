#* ************************************************************************** *#
#*                                                                            *#
#*                                                                            *#
#*   main.py                                                                  *#
#*                                                                            *#
#*   By: yhetman <yhetman@student.unit.ua>                                    *#
#*                                                                            *#
#*   Created: 2021/11/29 21:49:25 by yhetman                                  *#
#*   Updated: 2021/11/29 21:49:26 by yhetman                                  *#
#*                                                                            *#
#* ************************************************************************** *#

from random import randint

from gf import *
from consts import *
import os

def generate_privat(length):
    randint(1, ((1 << (length - 1)) - 1))



def generate_public(P, d):
    return multiply_by_elliptic_curve_order(negative_point(P), d)



def main():
    P = elliptic_curve_base_point()
    length = n.bit_length()

    d = generate_privat(length)

    Q = generate_public(P, d)






