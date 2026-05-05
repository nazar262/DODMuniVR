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

for B in range(1, 40):
    for r in range(P[B][B]):
        A = unrank(B, r)
        r_calc = rank(B, A)
        if r != r_calc:
            print(f"B={B}, r={r}, A={A}, rank={r_calc}")
            exit(1)
print("All matched!")
