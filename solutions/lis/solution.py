#!/usr/bin/env python3
import sys
import bisect

def solve():
    def get_tokens():
        for line in sys.stdin:
            for token in line.split():
                yield token

    tokens = get_tokens()
    try:
        T_str = next(tokens)
    except StopIteration:
        return
    T = int(T_str)
    
    out = []
    
    for _ in range(T):
        n = int(next(tokens))
        A = [int(next(tokens)) for _ in range(n)]
        
        # 1. max_len and sol_max_len
        dp_len = [0] * n
        tails = []
        tail_idx = []
        parent = [-1] * n
        
        for i in range(n):
            pos = bisect.bisect_left(tails, A[i])
            if pos == len(tails):
                tails.append(A[i])
                tail_idx.append(i)
            else:
                tails[pos] = A[i]
                tail_idx[pos] = i
            dp_len[i] = pos + 1
            if pos > 0:
                parent[i] = tail_idx[pos-1]
                
        max_len = len(tails)
        
        sol_max_len = [0] * n
        if max_len > 0:
            curr = tail_idx[-1]
            while curr != -1:
                sol_max_len[curr] = 1
                curr = parent[curr]
                
        cert_max_len = dp_len[:]
        
        sorted_unique = sorted(list(set(A)))
        val_to_idx = {v: i+1 for i, v in enumerate(sorted_unique)}
        max_val = len(sorted_unique)
        
        bit = [(0, -1)] * (max_val + 1)
        
        def query(index):
            res_sum = 0
            res_idx = -1
            while index > 0:
                if bit[index][0] > res_sum:
                    res_sum = bit[index][0]
                    res_idx = bit[index][1]
                index -= (index & -index)
            return res_sum, res_idx
            
        def update(index, val_sum, orig_idx):
            while index <= max_val:
                if val_sum > bit[index][0]:
                    bit[index] = (val_sum, orig_idx)
                index += (index & -index)
                
        dp_sum = [0] * n
        parent_sum = [-1] * n
        
        for i in range(n):
            v_idx = val_to_idx[A[i]]
            best_sum, best_idx = query(v_idx - 1)
            dp_sum[i] = best_sum + A[i]
            parent_sum[i] = best_idx
            update(v_idx, dp_sum[i], i)
            
        max_sum = 0
        best_end = -1
        for i in range(n):
            if dp_sum[i] > max_sum:
                max_sum = dp_sum[i]
                best_end = i
                
        sol_max_sum = [0] * n
        curr = best_end
        while curr != -1:
            sol_max_sum[curr] = 1
            curr = parent_sum[curr]
            
        out.append(str(max_len))
        out.append(" ".join(map(str, sol_max_len)))
        out.append(" ".join(map(str, cert_max_len)))
        out.append(str(max_sum))
        out.append(" ".join(map(str, sol_max_sum)))
        
    print("\n".join(out))

if __name__ == '__main__':
    solve()
