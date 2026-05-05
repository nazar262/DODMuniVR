#!/usr/bin/env python3
import sys

# Increase recursion depth just in case
sys.setrecursionlimit(20000)

BASE = 10**9 + 7

# P[n][k] = number of partitions of n into parts <= k
P = [[0] * 305 for _ in range(305)]
for k in range(305):
    P[0][k] = 1
for n in range(1, 305):
    for k in range(1, 305):
        P[n][k] = P[n][k-1]
        if n >= k:
            P[n][k] += P[n-k][k]

def a(B):
    total = P[B][B]
    return total >= BASE, total % BASE

def rank(B, A):
    r = 0
    budget = B
    for part in A:
        for p in range(budget, part, -1):
            r += P[budget - p][p]
        budget -= part
    return r

def unrank(B, r):
    ans = []
    budget = B
    max_val = B
    while budget > 0:
        max_val = min(max_val, budget)
        for p in range(max_val, 0, -1):
            cnt = P[budget - p][p]
            if r >= cnt:
                r -= cnt
            else:
                ans.append(p)
                budget -= p
                max_val = p
                break
    return ans

def solve():
    # Interactive reading token by token
    def get_tokens():
        for line in sys.stdin:
            for token in line.split():
                yield token

    tokens = get_tokens()
    
    try:
        T_str = next(tokens)
    except StopIteration:
        return
    T = int(T_str)
    
    for _ in range(T):
        B = int(next(tokens))
        r = int(next(tokens))
        
        A = []
        curr_sum = 0
        while curr_sum < B:
            part = int(next(tokens))
            A.append(part)
            curr_sum += part
            
        overflow, a_B = a(B)
        print(1 if overflow else 0, a_B)
        print(rank(B, A))
        print(" ".join(map(str, unrank(B, r))))

if __name__ == '__main__':
    solve()
