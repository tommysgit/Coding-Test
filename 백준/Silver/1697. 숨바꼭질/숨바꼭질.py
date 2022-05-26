from collections import deque


def bfs(v, target, visited):
    count = 0
    queue = deque()
    queue.append([v, count])
    while queue:
        v, count = queue.popleft()
        if v == target:
            return count
        for i in graph[v]:
            if not visited[i]:
                queue.append([i, count+1])
                visited[i] = True
    
N, K = map(int, input().split())
# X + 1  / X * 2
graph = [[]for i in range(100001)]
visited = [False]*(100001)
for i in range(100001):
    if i+1<len(graph):
        graph[i].append(i+1)
    if i-1>=0 and (i-1) not in graph[i]:
        graph[i].append(i-1)
    if 0<=i*2 and i*2<len(graph) and (i*2) not in graph[i] and i!=i*2:
        graph[i].append(i*2)
visited[N] = True
result = bfs(N, K, visited)
print(result)