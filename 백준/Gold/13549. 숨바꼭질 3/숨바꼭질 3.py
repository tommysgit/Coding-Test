from collections import deque


N, K = map(int, input().split())
MAX = 100001
cost = [-1]*MAX
is_visit = [0]*MAX
queue = deque()
queue.append(N)
cost[N] = 0
is_visit[N] = 1
while queue:
    num = queue.popleft()
    if num*2 < MAX and is_visit[num*2] == 0:
        is_visit[num*2] = 1
        cost[num*2] = cost[num]
        queue.appendleft(num*2)
    if num+1 < MAX and is_visit[num+1] == 0:
        is_visit[num+1] = 1
        cost[num+1] = cost[num] + 1
        queue.append(num+1)
    if num-1 >= 0 and is_visit[num-1] == 0:
        is_visit[num-1] = 1
        cost[num-1] = cost[num] + 1
        queue.append(num-1)
print(cost[K])
