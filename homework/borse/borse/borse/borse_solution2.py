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
    max_val = B
    for part in A:
        for p in range(max_val, part, -1):
            if budget >= p:
                r += P[budget - p][p]
        budget -= part
        max_val = part
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

def main():
    # Read all tokens from stdin
    data = sys.stdin.read().split()
    if not data: return
    T = int(data[0])
    idx = 1
    
    out = []
    for _ in range(T):
        B = int(data[idx])
        idx += 1
        r = int(data[idx])
        idx += 1
        
        A = []
        curr_sum = 0
        while curr_sum < B:
            part = int(data[idx])
            A.append(part)
            curr_sum += part
            idx += 1
            
        overflow, a_B = a(B)
        out.append(f"{1 if overflow else 0} {a_B}")
        out.append(str(rank(B, A)))
        out.append(" ".join(map(str, unrank(B, r))))
        
    print("\n".join(out))

if __name__ == '__main__':
    main()
