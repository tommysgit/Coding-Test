N = int(input())
lists = [list(map(int, input().split())) for i in range(N)]
output = []
graph = [[]for i in range(N)]
for i in range(N):
    for j in range(N):
        if lists[i][j] == 1:
            graph[i].append(j)
def dfs(graph,v, visited ):    
    for i in graph[v]:
        if visited[i] ==0:
            visited[i] = 1
            dfs(graph, i, visited)
    return visited
for i in range(N):
    visited = [0]*N
    output.append(dfs(graph, i, visited))
for i in range(len(output)):
    print(*output[i])