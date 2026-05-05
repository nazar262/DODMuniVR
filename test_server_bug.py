P = [[0] * 305 for _ in range(305)]
for k in range(305):
    P[0][k] = 1
for n in range(1, 305):
    for k in range(1, 305):
        P[n][k] = P[n][k-1]
        if n >= k:
            P[n][k] += P[n-k][k]

def rank_correct(B, A):
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

def rank_buggy(B, A):
    r = 0
    budget = B
    for part in A:
        for p in range(budget, part, -1):
            r += P[budget - p][p]
        budget -= part
    return r

# Find a partition of B=10 or 15 where rank_correct is 14 and rank_buggy is 15
def find_A():
    def get_parts(n, max_val):
        if n == 0: return [[]]
        ans = []
        for p in range(min(n, max_val), 0, -1):
            for tail in get_parts(n-p, p):
                ans.append([p] + tail)
        return ans
    
    for B in range(1, 20):
        parts = get_parts(B, B)
        for A in parts:
            rc = rank_correct(B, A)
            rb = rank_buggy(B, A)
            if rc == 14 and rb == 15:
                print(f"B={B}, A={A}, rc={rc}, rb={rb}")
                return
            if rc == 6 and rb == 13:
                print(f"B={B}, A={A}, rc={rc}, rb={rb}")
find_A()
