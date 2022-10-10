N, M = map(int, input().split())
A = list(map(int, input().split()))
ans = 0
left, right = 0, 1
while right <= N and left <= right:
    tmp_sum = sum(A[left:right])
    if tmp_sum == M:
        ans += 1
        right += 1
    elif tmp_sum < M:
        right += 1
    else:
        left += 1
print(ans)