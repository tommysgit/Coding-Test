import sys
sys.setrecursionlimit(100*1000)
N, M, K = map(int, (input().split()))
is_empty = [[True for col in range(M)] for row in range(N) ]
count = []
for i in range(K):
    r1, c1, r2, c2 = map(int, (input().split()))
    for r in range(r1,r2):
        for c in range(c1,c2):
            is_empty[c][r] = False
    
def dfs(is_empty,r,c, count):
    if r<=-1 or r>=N or c<=-1 or c>=M:
        return False
    if is_empty[r][c] == True:
        count.append(1)
        is_empty[r][c] = False
        dfs(is_empty, r-1,c, count)
        dfs(is_empty,r+1,c, count)
        dfs(is_empty,r,c-1, count)
        dfs(is_empty,r,c+1, count)
        return count
    return False
for i in range(N):
    for j in range(M):
        v = dfs(is_empty,i,j,[])
        if v != False:
            count.append(v)
count.sort()
print(len(count))
for i in range(len(count)):
    print(len(count[i]), end=' ')