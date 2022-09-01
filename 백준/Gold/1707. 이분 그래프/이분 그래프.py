# 1707
import sys
sys.setrecursionlimit(10**6)
K = int(input())
def dfs(node, is_visit, group, graph):
    is_visit[node] = group

    for next_node in graph[node]:
        # 이미 방문한 노드와 같은 그룹이면 False
        if is_visit[node] == is_visit[next_node]:
            return 0
        # 방문하지 않은 노드는 방문
        if not is_visit[next_node]:
            result = dfs(next_node, is_visit, -group, graph)
            if not result:
                return 0
    return 1

for i in range(K):
    V, E = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(V+1)]
    for j in range(E):
        A, B = map(int, sys.stdin.readline().split())
        graph[A].append(B)
        graph[B].append(A)
    is_visit = [0]*(V+1)
    result = 1
    for node in range(V+1):
        if is_visit[node] == 0:
            result = dfs(node, is_visit, 1, graph)
            if not result:
                break
    if result:
        print("YES")
    else:
        print("NO")