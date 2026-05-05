def buggy_g10(k, n):
    if n < k: return 1
    f = [1] * max(k + 1, n + 1)
    f[k] = 3
    for i in range(k + 1, n + 1):
        f[i] = (f[i-1] + f[i-k]) % 1000000007
    return f[n]

print("n=3, k=2:", buggy_g10(2, 3))
print("n=4, k=3:", buggy_g10(3, 4))
