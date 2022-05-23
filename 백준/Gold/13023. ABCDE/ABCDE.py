import sys
sys.setrecursionlimit(2000*2000)
N, M = map(int, input().split())
graph = [[] for i in range(N)]
visited = [False]*N
for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
def dfs(v, count):
    global ans
    visited[v] = True
    if count == 4:
        ans = True
        return
    
    for i in graph[v]: 
        if visited[i] == False:
            visited[i] = True
            dfs(i, count+1)
            visited[i] = False
    
for i in range(len(graph)):
    # 시작 위치에 따라 깊이가 다르다. 따라서 모든 경우의 수를 확인하기 위해 visited 초기화
    ans = False
    dfs(i, 0)
    visited[i] = False
    if ans == True:
        break

if ans:
    print(1)
else:
    print(0)