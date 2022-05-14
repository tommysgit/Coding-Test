N = int(input())
M = int(input())
edge = []
graph = [[] for i in range(N+1)]
visited = [False]*(N+1)
count = []
for i in range(M):
    a, b =map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if visited[i] == False:
            count.append(1)
            dfs(graph,i,visited)
dfs(graph,1,visited)
print(len(count))
