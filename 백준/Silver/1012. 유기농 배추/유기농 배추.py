import sys
T = int(input())
M = []
N = []
sys.setrecursionlimit(2500*T)
cor = []
dx = [-1, 1, 0, 0]
dy = [0,0,-1,1]
for i in range(T):
    m, n, K = map(int, input().split())
    M.append(m)
    N.append(n)
    tmp = []
    for j in range(K):
        x,y = (input().split())
        x = int(x)
        y = int(y)
        tmp.append([x,y])
    cor.append(tmp)
# cor의 리스트를 돌면서  상하 좌우로 이동한 값이 리스트에 있으면제거 후 이동, 없으면 카운트 +1
def warm(warm_bug,x ,y):
    
    if len(warm_bug) == 0:
        return
    warm_bug.remove([x,y])
    for i in range(4):
        mx = x+dx[i]
        my = y+dy[i]
        if [mx, my] in warm_bug: # 리스트에 없을 경우 통과  있을 경우 재귀
            warm(warm_bug, mx, my)
        else:
            continue

for i in range(T):
    animal = 0
    while len(cor[i]) !=0:
        animal+=1
        x, y = cor[i][len(cor[i])-1]
        warm(cor[i],x,y)
    print(animal)
        