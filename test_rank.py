P = [[0] * 305 for _ in range(305)]
for k in range(305):
    P[0][k] = 1
for n in range(1, 305):
    for k in range(1, 305):
        P[n][k] = P[n][k-1]
        if n >= k:
            P[n][k] += P[n-k][k]

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

def brute_force_partitions(n, max_val):
    if n == 0:
        return [[]]
    ans = []
    for p in range(min(n, max_val), 0, -1):
        for tail in brute_force_partitions(n - p, p):
            ans.append([p] + tail)
    return ans

B = 20
parts = brute_force_partitions(B, B)
for i, A in enumerate(parts):
    r = rank(B, A)
    if r != i:
        print(f"Error for {A}: expected {i}, got {r}")
        break
else:
    print("All correct for B=20")
