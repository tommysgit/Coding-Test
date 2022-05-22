from collections import deque


N = int(input())
graph = []
for i in range(N):
    graph.append(input())
complete = [[False for j in range(N)] for i in range(N)]
dx = [-1, 1, 0, 0]
dy = [0 , 0 , -1, 1]
def bfs(r,c):
    count = 1
    queue = deque()
    queue.append([r,c])
    complete[r][c] = True
    while queue:
        r, c = queue.popleft()
        for i in range(4):
            mx = r + dx[i]
            my = c + dy[i]
            if mx<0 or my<0 or mx>=N or my>=N:
                continue
            if graph[mx][my] == '0' or complete[mx][my] == True:
                continue
            complete[mx][my] = True
            count +=1
            queue.append([mx,my])
    return count
            
    
house = []
for i in range(len(graph)):
    for j in range(len(graph[i])):
        if graph[i][j] =='1' and complete[i][j] == False:
            house.append(bfs(i,j))
house.sort()
print(len(house))
for i in house:
    print(i)