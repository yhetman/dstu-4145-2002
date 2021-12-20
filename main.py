from random import randint
from hashlib import sha256
from gf import *
from consts import *
import os
from elliptic_curve_functionality import *

def generate_privat(length):
    if DEBUG: print("[DEBUG] : main : generate_privat")
    return randint(1, ((1 << (length - 1)) - 1))


def generate_public(P, d):
    if DEBUG: print("[DEBUG] : main : generate_public")
    return multiply_by_elliptic_curve_order(negative_point(P), d)


def generate_params():
    P = elliptic_curve_base_point()
    length = n.bit_length()
    # print(P)
    # print(length)
    d = generate_privat(length)
    print("Private key was generated: ", d)

    Q = generate_public(P, d)
    print("Public key was generated: ", Q)
    x,y = Q
    print(multiplication(y, y) ^ multiplication(x, y) ^ power(x, 3) ^ multiplication(A, multiplication(x, x)) ^ B)
    print(multiply_by_elliptic_curve_order(Q,n))
    return d,P,Q



def generate_presign(P):
    while True:
        # print('try')
        e = randint(1,2**(n.bit_length()-1))
        Fe = multiply_by_elliptic_curve_order(P, e)
        if Fe[0] != 0:
            return e, Fe[0]



def H(T):
    h = int(sha256(T.encode('utf-8')).hexdigest(), 16)
    if h == 0:
        return 1
    else:
        return h


def hash_to_galua(h):
    return h % (2 ** m)


def compute_signature(r,s):
    l = Ld // 2
    # print('signature computation')
    # print(l)
    # print(r.bit_length())
    # print(s.bit_length())
    return (s << l) + r


def de_compute_signature(D):
    l = Ld // 2
    r = D % (2**l)
    s = D >> l
    return r,s


def sign(T,P):
    h = H(T)
    h = hash_to_galua(h)
    while True:
        # print('try to sign')
        e,Fe = generate_presign(P)
        r = multiplication(h,Fe)
        if r == 0:
            continue
        s = (e + d * r) % n
        if s == 0:
            continue
        print('signature computed')
        D = compute_signature(r,s)
        print (D)
        print(r,s)
        print(r-n,s-n)
        r_, s_ = de_compute_signature(D)
        print(r_,s_)
        print(r_-n,s_-n)
        return D


def check_sign(T,D,P,Q):
    h = H(T)
    h = hash_to_galua(h)
    r,s = de_compute_signature(D)
    if r >= n or s >= n:
        print('HERE')
        print(r - n)
        print(s - n)
        return False
    sP = multiply_by_elliptic_curve_order(P,s)
    rQ = multiply_by_elliptic_curve_order(Q,r)
    R = sum_points(sP,rQ)
    y = multiplication(h, R[0])
    return r == y


if __name__ == '__main__':
    # input_ = input('Enter something: ')
    # h = int(sha256(input_.encode('utf-8')).hexdigest(),16)
    # print(h)
    # print(h.bit_length())
    # print(n.bit_length())
    d,P,Q = generate_params()
    T = 'test'
    D = sign(T,P)
    # e,Fe = generate_presign(P)
    print('signature')
    print(D)
    print(D.bit_length())
    print(check_sign(T,D,P,Q))
    print(check_sign(T, D+1, P, Q))
