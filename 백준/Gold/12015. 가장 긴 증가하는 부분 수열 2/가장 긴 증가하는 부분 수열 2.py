from bisect import bisect_left


N = int(input())
A = list(map(int, input().split()))

q = []
q.append(A[0])
for i, v in enumerate(A):
    if v > q[-1]:
        q.append(v)
    else:
        insert_idx = bisect_left(q, v)
        q[insert_idx] = v
print(len(q))