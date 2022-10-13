N = int(input())
A = list(map(int, input().split()))
d = [ 1 for i in range(N)]
for i in range(N):
    for j in range(i):
        if A[i] > A[j]:
            d[i] = max(d[i], d[j]+1)
print(max(d))