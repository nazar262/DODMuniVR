#!/usr/bin/env python3
from sys import stderr,stdout

BASE = 10**9 + 7

def a(B):
    """ where a_B is the number of assignments of B coins to the students, this function returns:
        1. False if a_B < BASE, otherwise True
        2. a_B % BASE
    """
    #print(f"called num_borse({a=}, {at_most=})", file=stderr)
    return False,42 

def rank(B, A):
    #print(f"called rank({B=}, {A=})", file=stderr)
    #assert sum(A) == B
    return 0

def unrank(B, r):
    #print(f"called unrank({B=}, {r=})", file=stderr)
    return [B-1,1]


T = int(input())
for t in range(1, 1 + T):
    B = int(input())
    r = int(input())
    A = list(map(int, input().strip().split()))
    overflow,a_B = a(B)
    print(1 if overflow else 0, a_B)
    print(rank(B, A))
    print(" ".join(map(str, unrank(B, r))))

