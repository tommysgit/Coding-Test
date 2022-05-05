from collections import deque
N, M = map(int, input().split())
maze = []

count = 1
visited = [[False for col in range(M)] for row in range(N)]
for i in range(N):
    row = str(input())
    rows = []
    for i in range(len(row)):
        rows.append(row[i])
    maze.append(rows)

def bfs(rows, r, c, visited):
    global count
    visited[r][c] = True
    queue = deque([[r,c, count]])
    while queue: # 
        count += 1
        cordinate = queue.popleft()
        r = cordinate[0]
        c = cordinate[1]
        count = cordinate[2]
        if r == N-1 and c == M-1:
            break
        up = r-1
        down = r+1
        left = c-1
        right = c+1
        move = [] # 좌우 아래 좌표중 갈 수 있는곳만 반환
        # up down은 -1 혹은 len이 N을 넘을 수 없고 left right는 -1 혹은 M을 넘을 수 없다.
        if up != -1 and rows[up][c] != '0':
            move.append([up, c, count+1])
        if down != N and rows[down][c] != '0':
            move.append([down, c, count+1])
        if left != -1 and rows[r][left] != '0':
            move.append([r,left, count+1])
        if right != M and rows[r][right] != '0':
            move.append([r,right, count+1])
            
      # move에는 방문 가능한 곳이 있다.
        for i in range(len(move)):
            if not visited[move[i][0]][move[i][1]]:
                queue.append(move[i])
                visited[move[i][0]][move[i][1]] = True
bfs(maze, 0, 0 , visited)
print(count)