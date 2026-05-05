#!/usr/bin/env python3
from sys import stderr,stdout

BASE = 10**9 + 7

def display_matrix(name, M):
    print(name, file=stderr)
    m = len(M); n = len(M[0])
    for row in M:
        print(" ".join(map(str, row)), file=stderr)

def triangolo(n, Tri):
    #print(f"called triangolo({n=}, {Tri=}\n", file=stderr)
    opt_val = 0 # correct when all numbers in the input triangle are zeros
    opt_sol = [1]*(n-1) # correct when all numbers in the input triangle are zeros
    num_opt_sols = 2**(n-1) % BASE # correct when all numbers in the input triangle are zeros
    opt_vals_constrained = [ [0]*(i+1) for i in range(n)]
    return opt_val, opt_sol, num_opt_sols, opt_vals_constrained 


T = int(input())
for t in range(1, 1 + T):
    n = int(input())
    Tri = []
    for _ in range(n):
        Tri.append(list(map(int, input().strip().split())))
    opt_val, opt_sol, num_opt_sols, opt_vals_constrained = triangolo(n, Tri)
    print(opt_val)
    print(" ".join(map(str,opt_sol)))
    print(num_opt_sols)
    for row in opt_vals_constrained:
        print(" ".join(map(str, row)))
