from collections import deque
import sys
sys.setrecursionlimit(5000*100)

N, M = map(int, input().split())
edge = []
for i in range(1,M+1):
    edge.append(list(map(int, input().split())))
graph = [[]for i in range(N+1)]
for i in range(len(edge)):
    tmp = edge[i]
    graph[tmp[0]].append(tmp[1])
    graph[tmp[1]].append(tmp[0])
# 그래프의 간선별로 자신을 제외한 노드간 거리의 합이 가장 작은 것을 출력한다.
kevin_bacon = []
def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = -1
    sum = 0
    d = [0]*(N+1)
    while queue: # count가 가중되어 더해진다 이를 수정해야함
        e = queue.popleft()
        for i in graph[e]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = 1
                d[i] = (d[e] +1) # 이전 노드의 처음까지와의 거리
    for i in range(len(d)):
        sum += d[i]
    return sum

for i in range(1, N+1): 
    # i번째 노드를 제외하고 타겟 노드를 설정하여 합의 값을 구한다.
    visited = [0] * (N+1)
    kevin_bacon.append((bfs(graph, i, visited)))
    
minimum = min(kevin_bacon)
print(kevin_bacon.index(minimum)+1)