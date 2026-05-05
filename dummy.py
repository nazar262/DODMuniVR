import sys
# read T
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    n = int(input())
    A = list(map(int, input().split()))
    print(5) # goal 1
    print(" ".join(["0"] * n)) # goal 2
    print(" ".join(["1"] * n)) # goal 3
    print(35) # goal 4
    print(" ".join(["0"] * n)) # goal 5
