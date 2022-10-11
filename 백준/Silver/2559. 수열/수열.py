from collections import deque


N, K = map(int, input().split())
arr = list(map(int, input().split()))
q = deque(arr[:K])
ans = -1e9
cur_sum = sum(q)
ans = max(ans, cur_sum)
for i in range(K, N):
    q.append(arr[i])
    sub_num = q.popleft()
    add_num = arr[i]
    cur_sum += add_num
    cur_sum -= sub_num
    ans = max(ans, cur_sum)
print(ans)