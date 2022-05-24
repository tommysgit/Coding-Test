# 7562
from collections import deque


T = int(input())
dx = [-1,-2,-2,-1,1,2,2,1]
dy = [-2,-1,1,2,-2,-1,1,2]

def bfs(graph, r, c):
    count = 0
    queue = deque()
    queue.append([r,c, count])
    while queue:
        r, c, count = queue.popleft()
        if r == target_r and c == target_c:
            return count
        for i in range(8):
            mx = r+dx[i]
            my = c+dy[i]
            if mx<0 or my<0 or mx>=I or my>=I:
                continue
            if graph[mx][my] == 0:
                queue.append([mx,my, count+1])
                graph[mx][my] = 1
output = []
for i in range(T):
    I = int(input()) # 체스판 크기
    cur_r, cur_c = map(int, input().split())
    target_r, target_c = map(int, input().split())
    graph = [[0]*I for i in range(I)]
    graph[cur_r][cur_c] = 1
    output.append(bfs(graph, cur_r, cur_c))
    
for i in output:
    print(i)