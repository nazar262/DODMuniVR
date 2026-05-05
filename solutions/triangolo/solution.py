#!/usr/bin/env python3
"""
Problem: triangolo  (90 points)
Technique: Dynamic Programming — Triangle max-path
Server:    wss://ta.di.univr.it/dodm

Given a triangle of n rows, find path from (0,0) to any cell in last row,
maximizing sum. At each row i you can go to (i+1, j) [same col = left]
or (i+1, j+1) [col+1 = right].

Output per test case:
  Line 1  : opt_val   — maximum path sum
  Line 2  : opt_sol   — n-1 direction choices: 1=right, -1=left (or ambiguous)
  Line 3  : num_opt_sols — number of optimal paths mod 10^9+7
  Lines...: opt_vals_constrained[i][j] — best path sum through cell (i,j)
"""
import sys
input = sys.stdin.readline

BASE = 10**9 + 7


def triangolo(n, Tri):
    INF = float('inf')

    # ── bot[i][j] = best path sum from (i,j) to bottom ───────────────────
    bot = [[0]*(i+1) for i in range(n)]
    for j in range(n):
        bot[n-1][j] = Tri[n-1][j]
    for i in range(n-2, -1, -1):
        for j in range(i+1):
            bot[i][j] = Tri[i][j] + max(bot[i+1][j], bot[i+1][j+1])

    opt_val = bot[0][0]

    # ── top[i][j] = best path sum from (0,0) to (i,j) ───────────────────
    top = [[-INF]*(i+1) for i in range(n)]
    top[0][0] = Tri[0][0]
    for i in range(1, n):
        for j in range(i+1):
            # came from (i-1, j) [left, same col]
            if j <= i-1 and top[i-1][j] > -INF:
                top[i][j] = max(top[i][j], top[i-1][j] + Tri[i][j])
            # came from (i-1, j-1) [right, col+1]
            if j >= 1 and top[i-1][j-1] > -INF:
                top[i][j] = max(top[i][j], top[i-1][j-1] + Tri[i][j])

    # ── opt_vals_constrained[i][j] ────────────────────────────────────────
    opt_vals_constrained = []
    for i in range(n):
        row = []
        for j in range(i+1):
            if top[i][j] > -INF:
                row.append(top[i][j] + bot[i][j] - Tri[i][j])
            else:
                row.append(0)
        opt_vals_constrained.append(row)

    # ── num_opt_sols ──────────────────────────────────────────────────────
    # cnt[i][j] = # optimal paths from (0,0) to (i,j) achieving top[i][j]
    cnt = [[0]*(i+1) for i in range(n)]
    cnt[0][0] = 1
    for i in range(1, n):
        for j in range(i+1):
            if top[i][j] == -INF:
                continue
            # from (i-1, j) going left (same col)
            if j <= i-1 and top[i-1][j] + Tri[i][j] == top[i][j]:
                cnt[i][j] = (cnt[i][j] + cnt[i-1][j]) % BASE
            # from (i-1, j-1) going right (col+1)
            if j >= 1 and top[i-1][j-1] + Tri[i][j] == top[i][j]:
                cnt[i][j] = (cnt[i][j] + cnt[i-1][j-1]) % BASE

    num_opt_sols = 0
    for j in range(n):
        if top[n-1][j] + bot[n-1][j] - Tri[n-1][j] == opt_val:
            num_opt_sols = (num_opt_sols + cnt[n-1][j]) % BASE

    # ── opt_sol: direction at each step along the chosen optimal path ─────
    # Trace path greedily: at (i, col), go to whichever of (i+1,col) or
    # (i+1,col+1) gives a higher best-path value. If tie: ambiguous → -1.
    # opt_sol[k] = direction taken at step k:
    #   -1 = go left (same col) OR ambiguous (both equally good)
    #    1 = go right (col + 1) exclusively better
    opt_sol = []
    col = 0
    for i in range(n - 1):
        # best path through (i+1, col)   [go left]
        left_val  = top[i][col] + Tri[i+1][col]   + bot[i+1][col]   - Tri[i+1][col]   # = top[i][col] + bot[i+1][col]
        # best path through (i+1, col+1) [go right]
        right_val = top[i][col] + Tri[i+1][col+1] + bot[i+1][col+1] - Tri[i+1][col+1] # = top[i][col] + bot[i+1][col+1]

        left_total  = top[i][col] + bot[i+1][col]
        right_total = top[i][col] + bot[i+1][col+1]

        if right_total > left_total:
            opt_sol.append(1)
            col += 1
        else:
            # left is better or tied → -1
            opt_sol.append(-1)
            # col stays

    return opt_val, opt_sol, num_opt_sols, opt_vals_constrained


T = int(input())
for t in range(1, 1 + T):
    n = int(input())
    Tri = []
    for _ in range(n):
        Tri.append(list(map(int, input().strip().split())))
    opt_val, opt_sol, num_opt_sols, opt_vals_constrained = triangolo(n, Tri)
    print(opt_val)
    print(" ".join(map(str, opt_sol)))
    print(num_opt_sols)
    for row in opt_vals_constrained:
        print(" ".join(map(str, row)))
