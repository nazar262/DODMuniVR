#!/usr/bin/env python3
"""
Problem: first_PD  (64 points)
Technique: Dynamic Programming on a line/array
Server:    wss://ta.di.univr.it/dodm

Problem: Given array A of n values in [0,100), choose subset S of indices
such that any two chosen indices differ by >= 3.  Maximize sum of A[i] for i in S.

Output per test case (4 goals):
  1. count_feas_sols : f(n) mod BASE  — total feasible subsets
  2. optval          : maximum achievable sum
  3. optsol          : space-separated indices of one optimal solution (blank line if empty)
  4. count_opt_sols  : number of optimal solutions mod BASE
"""
import sys
input = sys.stdin.readline

BASE = 10**9 + 7


def solve(n, A):
    # ── 1. count_feas_sols ────────────────────────────────────────────────
    # f(n) = f(n-1) + f(n-3),  f(0)=1, f(1)=2, f(2)=3
    f = [0] * (n + 1)
    for i in range(n + 1):
        if i == 0:   f[i] = 1
        elif i == 1: f[i] = 2
        elif i == 2: f[i] = 3
        else:        f[i] = (f[i-1] + f[i-3]) % BASE
    count_feas = f[n]

    # ── 2. optval via DP ─────────────────────────────────────────────────
    # dp[i] = max value using only indices from {0..i}
    # dp[i] = max(dp[i-1],  A[i] + dp[i-3])   (dp[j]=0 for j<0)
    dp = [0] * n
    for i in range(n):
        no_take = dp[i-1] if i >= 1 else 0
        take    = A[i] + (dp[i-3] if i >= 3 else 0)
        dp[i]   = max(no_take, take)
    optval = dp[n-1] if n > 0 else 0

    # ── 3. optsol: reconstruct one optimal solution ───────────────────────
    sol = []
    i = n - 1
    while i >= 0:
        no_take = dp[i-1] if i >= 1 else 0
        take    = A[i] + (dp[i-3] if i >= 3 else 0)
        if take > no_take:          # must take i
            sol.append(i)
            i -= 3
        elif take == dp[i] == no_take:  # both optimal — prefer not-take for lex
            i -= 1
        else:                       # must not take i
            i -= 1
    sol.sort()

    # ── 4. count_opt_sols ─────────────────────────────────────────────────
    # cnt[i] = # feasible subsets of {0..i} achieving dp[i]
    # cnt[i]  += cnt[i-1]  if dp[i-1] == dp[i]            (not taking i)
    # cnt[i]  += cnt[i-3]  if A[i]+dp[i-3] == dp[i]       (taking i)
    #          (use 1 instead of cnt[j] when j < 0, i.e. empty prefix)
    cnt = [0] * n
    for i in range(n):
        # not-take branch
        prev_opt = dp[i-1] if i >= 1 else 0
        if prev_opt == dp[i]:
            cnt[i] = (cnt[i] + (cnt[i-1] if i >= 1 else 1)) % BASE
        # take branch
        left_opt = dp[i-3] if i >= 3 else 0
        if A[i] + left_opt == dp[i]:
            cnt[i] = (cnt[i] + (cnt[i-3] if i >= 3 else 1)) % BASE
    count_opt = cnt[n-1] if n > 0 else 1

    return count_feas, optval, sol, count_opt


T = int(input())
for _ in range(T):
    n = int(input())
    A = list(map(int, input().split()))
    count_feas, optval, sol, count_opt = solve(n, A)
    print(count_feas)
    print(optval)
    print(" ".join(map(str, sol)))   # blank line when sol is empty — correct!
    print(count_opt)
