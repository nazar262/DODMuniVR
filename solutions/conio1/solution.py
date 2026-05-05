#!/usr/bin/env python3
"""
Problem: conio1  (40 points)
Technique: Greedy — Coin Change
Server:    wss://ta.di.univr.it/dodm

Given amount S (euro-cents), find minimum number of coins using euro denominations.
Euro denominations (cents): 1, 2, 5, 10, 20, 50, 100, 200, 500, 1000
Greedy is optimal for euro coin system.

Output per test case:
  Line 1: optval  (minimum number of coins)
  Line 2: 10 counts for each denomination (space-separated)
"""
import sys
input = sys.stdin.readline

pieces = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000]


def solve(S):
    counts = [0] * len(pieces)
    remaining = S
    for i in range(len(pieces) - 1, -1, -1):
        counts[i] = remaining // pieces[i]
        remaining -= counts[i] * pieces[i]
    optval = sum(counts)
    return optval, counts


T = int(input())
for _ in range(T):
    S = int(input())
    optval, counts = solve(S)
    print(optval)
    print(" ".join(map(str, counts)))
