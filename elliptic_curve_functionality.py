#* ************************************************************************** *#
#*                                                                            *#
#*                                                                            *#
#*   elliptic_curve_functionality.py                                          *#
#*                                                                            *#
#*   By: yhetman <yhetman@student.unit.ua>                                    *#
#*                                                                            *#
#*   Created: 2021/11/29 21:49:25 by yhetman                                  *#
#*   Updated: 2021/11/29 21:49:26 by yhetman                                  *#
#*                                                                            *#
#* ************************************************************************** *#

from consts import *
from gf import *


def negative_point(point): # P -> -P
    return (point[0], point[0] ^ point[1])


def sum_points(p1, p2):
    if p1 == O: return p2
    if p2 == O: return p1
    if p1 == p2: return sum_point_twice(p1)
    if p2 == negative_point(p1): return O
    x_XOR = p1[0] ^ p2[0]
    y_XOR = p1[1] ^ p2[1]
    t = division(y_XOR, x_XOR)
    x = ((multiplication(t, t) ^ t) ^ x_XOR) ^ A
    y = (multiplication(t, p1[0] ^ x) ^ x) ^ p1[1]
    return (x, y)



def sum_point_twice(p):
    t = p[0] ^ division(p[1], p[0])
    x = (multiplication(t, t) ^ t) ^ A
    y = multiplication(p[0], p[0]) ^ multiplication(t ^ 1,  x)
    return (x, y)



def tr(x): 	# tr(x) - trace function
    t = x
    if DEBUG: print("[DEBUG] : tr") 
    for _ in range(m - 1):
        t = multiplication(t, t) ^ x
    return t



def htr(x):	# htr(x) - half-trace function
    t = x
    if DEBUG: print("[DEBUG] : htr") 
    for _ in range((m - 1) // 2):
        t = power(t, 4) ^ x
    return t



def equation_solution(u, w):	# solve the quadratic equation
    if DEBUG: print("[DEBUG] : equation_solution") 
    if u == 0: return (power(w, 1 << (m - 1)), 1)
    if w == 0: return (0, 2)
    inv_u = inverse(u)
    v = multiplication(w, multiplication(inv_u, inv_u))
    if tr(v) == 1: return O
    t = htr(v)
    z = multiplication(t, u)
    return (z, 2)



def random_point_generating():
    if DEBUG: print("[DEBUG] : elliptic_curve_base_point : random_point_generating")
    while True:
        u = randint(0, prim_eleme)
        w = (power(u, 3) ^ multiplication(A, multiplication(u, u))) ^ B
        (z, k) = equation_solution(w, u)
        if k > 0:
            return (u, z)



def multiply_by_elliptic_curve_order(P, k):   # k - elliptic curve order
    k_p = O
    if DEBUG: print("[DEBUG] : multiply_by_elliptic_curve_order")
    while k > 0:
        if k & 1 == 1:
            k_p = sum_points(k_p, P)
        P = sum_point_twice(P)
        k = k >> 1
    return k_p



def elliptic_curve_base_point():
    if DEBUG: print("[DEBUG] : elliptic_curve_base_point")
    while True:
        P = random_point_generating()
        R = multiply_by_elliptic_curve_order(P, n)
        if R == O:
            return P