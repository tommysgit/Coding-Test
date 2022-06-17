from collections import deque
import sys
N, M = map(int, input().split())
graph = [list(sys.stdin.readline()) for i in range(N)]
nx = [-1, 1, 0, 0]
ny = [0, 0, -1, 1]
result = []
min_cnt = N*M
def bfs(graph, x,y):
    queue = deque()
    queue.append((0,0,1))
    visited[x][y][1] = 1
    while queue:
        x, y, chance = queue.popleft()
        #print(x,y,chance, visited[x][y][chance])
        if x == N-1 and y == M-1:
            return visited[x][y][chance]
        for i in range(4):
            mx = x + nx[i]
            my = y + ny[i]
            if mx < 0 or my < 0 or mx>=N or my>=M:
                continue
            # 이미 방문한 곳인지 확인
            if visited[mx][my][chance] != 0:
                continue
            # 가려는 곳이 0인 경우 그냥 간다.
            if graph[mx][my] == '0':
                queue.append((mx, my, chance))
                visited[mx][my][chance] = visited[x][y][chance] + 1
            # 벽인 경우와 현재 기회가 있으면
            elif graph[mx][my] == '1' and chance == 1:
                queue.append((mx,my,0))
                visited[mx][my][0] = visited[x][y][chance] + 1

    return -1
# 벽을 부수고 온 상태와 부수고 오지 않은 상태를 구분하기 위해 무조건 3차원 배열이 필요하다.
visited = [list([0]*2 for j in range(M) ) for i in range(N)]


print(bfs(graph, 0, 0))