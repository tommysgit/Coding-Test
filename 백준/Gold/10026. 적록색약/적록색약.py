import sys
sys.setrecursionlimit(100*1000)
N = int(input())
blind_color = ['R', 'G']
rows = []
stack = []
visited1 = [[False for col in range(N)] for row in range(N)]
visited2 = [[False for col in range(N)] for row in range(N)]

for i in range(N):
    rows.append(str(input()))
    
def dfs(rows, r, c, visited, is_blind, prev):
    if r <= -1 or r>=N or c <= -1 or c>=N:
        return False
    if visited[r][c] == False: # 방문 처리되지 않은 노드와 이전노드를 확인
        if prev == '':
            prev = rows[r][c]
        if is_blind == False and prev == rows[r][c]:
           visited[r][c] = True
           dfs(rows,r-1,c,visited, is_blind, rows[r][c])
           dfs(rows, r+1, c, visited, is_blind, rows[r][c])
           dfs(rows, r, c-1, visited, is_blind, rows[r][c])
           dfs(rows, r, c+1, visited, is_blind, rows[r][c])
           return True 
        if is_blind == True: # 이 전이 R or G이면 R or G여야하고 B이면 B여야함
            if (prev == 'B' and rows[r][c] == 'B') or (prev in blind_color and rows[r][c] in blind_color):
               visited[r][c] = True
               dfs(rows,r-1,c,visited, is_blind, rows[r][c])
               dfs(rows, r+1, c, visited, is_blind, rows[r][c])
               dfs(rows, r, c-1, visited, is_blind, rows[r][c])
               dfs(rows, r, c+1, visited, is_blind, rows[r][c])
               return True 
    return False
origin = 0
blind = 0
for i in range(N):
    for j in range(N):
        if dfs(rows, i,j,visited1,False, ''):
            origin+=1
        if dfs(rows, i,j,visited2,True, ''):
            blind+=1
print(origin, blind)