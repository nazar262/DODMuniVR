A = [5, 3, 6, 4, 2, 8, 1, 7, 8, 9, 9, 9, 9]

# Find all LIS
from itertools import combinations
lis_len = 5
all_lis_indices = []
for indices in combinations(range(len(A)), lis_len):
    seq = [A[i] for i in indices]
    if all(seq[i] < seq[i+1] for i in range(lis_len-1)):
        all_lis_indices.append(indices)

print(f"Number of strict LIS: {len(all_lis_indices)}")

all_non_dec_indices = []
for indices in combinations(range(len(A)), lis_len):
    seq = [A[i] for i in indices]
    if all(seq[i] <= seq[i+1] for i in range(lis_len-1)):
        all_non_dec_indices.append(indices)

print(f"Number of non-decreasing LIS: {len(all_non_dec_indices)}")

# What else could be 35?
# Sum of LIS length ending at i?
lengths = [1, 1, 2, 2, 1, 3, 1, 3, 4, 5, 5, 5, 5]
print("Sum of lengths array:", sum(lengths))

# What about the lexicographical first / last binary strings?
# 0 1 0 1 0 0 0 1 1 0 0 0 1
# 1 0 1 0 0 0 0 1 1 0 0 0 1
