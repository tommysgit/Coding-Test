# 4963
from collections import deque
import sys
dx = [-1,1,0,0, -1, -1, 1, 1]
dy = [0,0,-1,1, -1, 1, -1, 1]

def bfs(graph, r, c):
    queue = deque()
    queue.append([r,c])
    graph[r][c] = -1
    while queue:
        r, c = queue.popleft()
        for i in range(8):
            mx = r + dx[i]
            my = c + dy[i]
            if mx<0 or my<0 or mx>=h or my>=w:
                continue
            if graph[mx][my] == 1:
                queue.append([mx,my])
                graph[mx][my] = -1
            
output = []
while True:
    w, h = map(int, sys.stdin.readline().split())
    if w==0 and h == 0:
        break
    graph = [list(map(int,sys.stdin.readline().split())) for _ in range(h)]
    count = 0
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if graph[i][j] == 1:
                bfs(graph, i,j)
                count+=1
    output.append(count)
for i in output:
    print(i)