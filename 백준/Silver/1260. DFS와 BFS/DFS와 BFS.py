from collections import deque


N, M ,V = map(int, input().split())
graph = [list(map(int, input().split())) for i in range(M)]
graph.insert(0, list())
visited1 = [False] * (N+1)
visited2 = [False] * (N+1)
order1 = []
order2 = []
def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    order1.append(v)
    tmp = []
    # graph를 돌면서 가장 작은 정점을 확인후 돌지 않았으면 돌고 아니면 나와서 다른 정점을 찾는다.
    for i in range(1,len(graph)):
        if v in graph[i]:
            for j in range(len(graph[i])):
                if graph[i][j]!=v:
                    tmp.append(graph[i][j])
    tmp.sort()
    for i in tmp:
        if not visited[i]:
            dfs(graph, i, visited)
def bfs(graph, v, visited):
    visited[v] = True # 첫 방문 True 처리
    queue = deque([v]) # queue초기화
    while queue: # queue가 빌떄까지 반복
        e = queue.popleft() # 돌때마다 pop후 출력
        order2.append(e)
        tmp = []
        # graph에 e와 연결된 간선들을 찾고 돌지 않은 정점을 작은 수 부터 돈다.
        for i in range(1, len(graph)):
            if e in graph[i]:
                for j in range(len(graph[i])):
                    if graph[i][j] != e and graph[i][j] not in tmp:
                        tmp.append(graph[i][j])
        tmp.sort()
        for i in tmp:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
    
    
dfs(graph, V, visited1)
bfs(graph, V, visited2)
for i in range(len(order1)):
    if i == len(order1)-1:
        print(order1[i])
    else:
        print(order1[i], end=' ')
for i in range(len(order2)):
    print(order2[i], end=' ')