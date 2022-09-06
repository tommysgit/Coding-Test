N = int(input())
visit = [-1]*N
answer = 0
def check(row):
    for nth_row in range(row):
        if visit[nth_row] == visit[row] or row-nth_row == abs(visit[nth_row] - visit[row]):
            return False
    return True
        
    pass
def dfs(row):
    #print(row)
    global answer
    if row == N:
        answer += 1
        return
    # visit[row] 의 가능한 값으로 dfs
    # 0부터 N까지 가능한 col 값을 구한다.
    for col in range(N):
        visit[row] = col
        if check(row):
            dfs(row+1)
dfs(0)
print(answer)