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
from elliptic_curve_functionality import *

def generate_privat(length):
    if DEBUG: print("[DEBUG] : main : generate_privat")
    randint(1, ((1 << (length - 1)) - 1))



def generate_public(P, d):
    if DEBUG: print("[DEBUG] : main : generate_public")
    return multiply_by_elliptic_curve_order(negative_point(P), d)


def main():
    P = elliptic_curve_base_point()
    length = n.bit_length()
    d = generate_privat(length)
    print("Privat key was generated: ", d)

    Q = generate_public(P, d)
    print("Public key was generated: ", Q)




if __name__ == '__main__':
    main()
