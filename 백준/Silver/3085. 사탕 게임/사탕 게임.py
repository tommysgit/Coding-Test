# 3085
from copy import deepcopy
N = int(input())
dx = [-1, 1, 0, 0]
dy = [0,0,-1,1]
candy = []
max_candy = 0
duple = []
def find_max(candy,a,b, color):
    up = a-1
    down = a+1
    left = b -1
    right = b +1
    count1 = 1
    count2 = 1
    while up>=0:
        if candy[up][b] != color:
            break
        count1+=1
        up -=1
    while down<N:
        if candy[down][b] != color:
            break
        count1+=1
        down +=1    
    while left>=0:
        if candy[a][left] != color:
            break
        count2+=1
        left -=1
    while right<N:
        if candy[a][right] != color:
            break
        count2+=1
        right +=1
    return max(count1, count2)
for i in range(N):
    candy.append(list(input()))
for i in range(len(candy)):
    for j in range(len(candy[i])):
        for k in range(4):
            mx = i + dx[k]
            my = j + dy[k]
            if mx<0 or my<0 or mx>=N or my>=N:
                continue
            if [[i,j], [mx,my]] in duple:
                continue
            duple.append([[mx,my],[i,j]])
            tmp = deepcopy(candy)
            tmp[i][j], tmp[mx][my] = tmp[mx][my], tmp[i][j]
            origin1 = find_max(candy, i,j, candy[i][j])
            change1 = find_max(candy, mx,my, candy[mx][my])
            origin2 = find_max(tmp, i,j, tmp[i][j])
            change2 = find_max(tmp, mx,my, tmp[mx][my])
            max_candy = max(max_candy, origin1, change1, origin2, change2)

print(max_candy)
        