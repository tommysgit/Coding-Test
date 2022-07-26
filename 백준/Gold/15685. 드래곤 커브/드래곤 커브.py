from copy import deepcopy


N = int(input())
# d 방향 / 0 x좌표 증가 / 1 y좌표 감소 / 2 x좌표 감소 / 3 y좌표 증가
curve_list =[]
graph = [[0]*101 for i in range(101)]
def up_direction(d):
    if d == 3:
        return 0
    else:
        return d+1
def insert(x,y,d, curve):
    if d == 0:
        x += 1
    elif d == 1:
        y -= 1
    elif d == 2:
        x -= 1
    else:
        y += 1
    curve.append((x,y,d))
    graph[x][y] = 1
# 4 2 1 / 4 1 2 / 3 1 3 / 3 2 2 / 2 2 3
def dragon_curve(curve, cur, g):
    if cur == g:
        return deepcopy(curve)
    #print(curve, cur, g)
    # curve에 있는 좌표, 방향을 읽어 삽입
    # 좌표는 바로 직전 좌표, 방향은 대칭되는 시점
    for i in reversed(range(1, len(curve))):
        tx,ty,d = curve[i]
        x,y,td = curve[-1]
        d = up_direction(d)
        insert(x,y,d,curve)
    return dragon_curve(curve, cur+1, g)

def check_square():
    count = 0
    for i in range(100):
        for j in range(100):
            if graph[i][j] == 1 and graph[i+1][j] == 1 and graph[i][j+1] == 1 and graph[i+1][j+1] == 1:
                count += 1
    return count
for i in range(N):
    x, y, d, g = map(int, input().split())
    graph[x][y] = 1
    tmp = []
    tmp.append((x,y,d))
    insert(x,y,d,tmp)
    if g == 0:
        curve_list.append(deepcopy(tmp))
    else:
        curve_list.append(dragon_curve(tmp, 0, g))
#print(curve_list)
print(check_square())