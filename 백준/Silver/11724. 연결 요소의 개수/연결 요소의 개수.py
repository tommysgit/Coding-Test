# 11724
import sys
N, M = map(int, input().split())
sys.setrecursionlimit(1000*1000)
visited = [False]*(N+1)
graph = [[] for _ in range(N+1)]
for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
    
def dfs(v):
    visited[v] = True
    
    for i in graph[v]:
        if visited[i] == False:
            dfs(i)
count = 0
for i in range(1,len(graph)):
    if visited[i] == False:
        dfs(i)
        count+=1
print(count)