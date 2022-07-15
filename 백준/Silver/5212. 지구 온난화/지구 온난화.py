from copy import deepcopy
import sys
from tabnanny import check
R, C = map(int, sys.stdin.readline().split())
graph = [sys.stdin.readline().strip() for i in range(R)]
result = []
cor_list = []
nx = [-1, 1, 0, 0]
ny = [0, 0, -1, 1]
min_r = R
min_c = C
max_r = 0
max_c = 0
def check_sea(r, c):
    count = 0
    for i in range(4):
        mr = r + nx[i]
        mc = c + ny[i]
        if mr < 0 or mc < 0 or mr >= R or mc >= C:
            count += 1
            continue
        if graph[mr][mc] == '.':
            count += 1
    if count >= 3:
        return 0
    else:
        return 1

for i in range(R):
    tmp = []
    for j in range(C):
        if graph[i][j] == 'X':
            is_sea = check_sea(i,j)
            if is_sea:
                tmp.append('X')
                cor_list.append((i,j))
            else:
                tmp.append('.')
        else:
            tmp.append(graph[i][j])
    result.append(deepcopy(tmp))
# 직사각형 범위 찾기
for i in cor_list:
    r, c = i
    if r >= max_r:
        max_r = r
    if r <= min_r:
        min_r = r
    if c >= max_c:
        max_c = c
    if c <= min_c:
        min_c = c
# 사각형 크기만큼 출력
for i in range(min_r, max_r+1):
    print(''.join(result[i][min_c:max_c+1]))