from collections import deque
import copy
import time

N, M = map(int, input().split())
dx = [-1, 1, 0 , 0]
dy = [0, 0, -1, 1]
minimum = 0
wall_list = []
empty_list = []
virus_list = []
graph = []
for i in range(N):
    lists =list(map(int, input().split()))
    graph.append(lists)
    for j in range(len(lists)):
        if graph[i][j] == 0:
            empty_list.append([i,j])
        elif graph[i][j] == 2:
            virus_list.append([i,j])
# 바이러스의 초기위치를 기억하고 
# 바이러스 2가 bfs를 돌때마다 맞붙어있는 0의 개수가 3이될때까지 반복  
def find_zero(graph):
    count = 0
    for i in range(len(empty_list)):
        x,y = empty_list[i]
        if graph[x][y] == 0:
            count+=1
    return count


def bfs(graph, x,y):
    queue = deque()
    queue.append((x,y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or nx>=N or ny<0 or ny>=M: # 이동할 방향이 범위를 넘어가거나
                continue
            if graph[nx][ny] == 1 or graph[nx][ny] == 2: # 벽이거나 바이러스일경우
                continue
            graph[nx][ny] = 2
            queue.append((nx, ny))
    return graph
            
#start = time.time()
for i in range(len(empty_list)):
    for j in range(i):
        for k in range(j):
            copy_graph = copy.deepcopy(graph)
            x1, y1 = empty_list[i]
            x2, y2 = empty_list[j]
            x3, y3 = empty_list[k]
            copy_graph[x1][y1] = 1
            copy_graph[x2][y2] = 1
            copy_graph[x3][y3] = 1
            for v in range(len(virus_list)):
                x,y = virus_list[v]
                bfs(copy_graph,x,y)
            tmp =find_zero(copy_graph)
            if tmp>minimum:
                minimum = tmp
#print(time.time()-start)
print((minimum))