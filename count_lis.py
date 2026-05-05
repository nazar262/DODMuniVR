def count_lis(A):
    n = len(A)
    dp = [1] * n
    cnt = [1] * n
    for i in range(n):
        for j in range(i):
            if A[j] < A[i]:
                if dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    cnt[i] = cnt[j]
                elif dp[j] + 1 == dp[i]:
                    cnt[i] += cnt[j]
    max_len = max(dp)
    total_lis = sum(cnt[i] for i in range(n) if dp[i] == max_len)
    return total_lis

print("A1:", count_lis([5, 3, 6, 4, 2, 8, 1, 7, 8, 9, 9, 9, 9]))
print("A2:", count_lis([5, 3, 6, 4, 12, 8, 1, 7, 18, 15, 9, 19, 16]))
print("A3:", count_lis([4, 12, 8, 1, 7, 18, 15, 9, 19, 16, 8, 15, 13, 16]))
