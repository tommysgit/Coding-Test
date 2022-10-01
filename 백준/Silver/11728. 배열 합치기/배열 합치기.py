N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort()
B.sort()
a, b = 0, 0
ans = []
while 1:
    if a >= N or b >= M:
        break
    if A[a] < B[b]:
        ans.append(A[a])
        a += 1
    elif A[a] > B[b]:
        ans.append(B[b])
        b += 1
    else:
        ans.append(A[a])
        ans.append(B[b])
        a += 1
        b += 1
if a < N:
    ans += A[a:]
if b < M:
    ans += B[b:]
print(*ans)