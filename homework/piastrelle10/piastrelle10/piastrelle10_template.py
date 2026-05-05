#!/usr/bin/env python3
from sys import stderr, setrecursionlimit
from functools import lru_cache

setrecursionlimit(50000)

BASE = 10**9 + 7

@lru_cache(maxsize=None)
def num_1xn_with_1x1_and_1x2(n):
    assert n >= 0
    return 42 % BASE
    
@lru_cache(maxsize=None)
def num_2xn_with_1x1_and_1x2(n):
    assert n >= 0
    return 42 % BASE

@lru_cache(maxsize=None)
def num_2xn_with_1x1_and_2x1(n):
    assert n >= 0
    return 42 % BASE

@lru_cache(maxsize=None)
def num_2xn_with_1x1_and_1x2_and_2x1(n):
    assert n >= 0
    return 42 % BASE
    
@lru_cache(maxsize=None)
def num_2xn_with_1x1_and_1x2_and_2x1_and_2x2(n):
    assert n >= 0
    return 42 % BASE
    
@lru_cache(maxsize=None)
def num_1xn_with_1xall(n):
    assert n >= 0
    return 42 % BASE
    
@lru_cache(maxsize=None)
def num_kxn_with_1xall(n,k):
    assert n >= 0
    assert k >= 1
    return 42 % BASE
    
@lru_cache(maxsize=None)
def num_kxn_with_1xall_and_kx1(n,k):
    assert n >= 0
    assert k >= 1
    return 42 % BASE
    
@lru_cache(maxsize=None)
def num_kxn_with_1xk_and_kx1(n,k):
    assert n >= 0
    assert k >= 1
    return 42 % BASE
    
@lru_cache(maxsize=None)
def num_kxn_with_1xk_and_kx1_and_kxk(n,k):
    assert n >= 0
    assert k >= 1
    return 42 % BASE    


T = int(input())
for t in range(1, 1 + T):
    n,k = map(int, input().strip().split())
    print(num_1xn_with_1x1_and_1x2(n))         #goal 1
    print(num_2xn_with_1x1_and_1x2(n))         #goal 2
    print(num_2xn_with_1x1_and_2x1(n))         #goal 3
    print(num_2xn_with_1x1_and_1x2_and_2x1(n))         #goal 4
    print(num_2xn_with_1x1_and_1x2_and_2x1_and_2x2(n)) #goal 5
    print(num_1xn_with_1xall(n))                  #goal 6
    print(num_kxn_with_1xall(n,k))                #goal 7
    print(num_kxn_with_1xall_and_kx1(n,k))        #goal 8
    print(num_kxn_with_1xk_and_kx1(n,k))          #goal 9
    print(num_kxn_with_1xk_and_kx1_and_kxk(n,k))  #goal 10
