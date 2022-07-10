# 16918
R, C, N = map(int, input().split())
graph = [list(input()) for i in range(R)]
# . 빈칸 , 0 폭탄
# 설치한 폭탄이 터지고 다음 초에 바로 빈 공간에 폭탄 설치
# -1, 1 / 0, 2 / 1, . / 2, -1 / . , 0
# 싸이클이 존재한다.
nr = [-1, 1, 0, 0]
nc = [0, 0, -1, 1]
order = ['.', 0, 1, 2]
time = 1
def bomb(r, c):
    graph[r][c] = '.'
    for i in range(4):
        mr = r + nr[i]
        mc = c + nc[i]
        #print(mr,mc)
        if mr < 0 or mc < 0 or mr >= R or mc >= C:
            continue
        graph[mr][mc] = '.'

def time_pass():
    bomb_list = []
    for i in range(R):
        for j in range(C):
            if graph[i][j] == 2:
                bomb_list.append((i,j))
            else:
                next_order = order.index((graph[i][j])) + 1
                graph[i][j] = order[next_order]
                
    return bomb_list

def to_zero():
    for i in range(R):
        for j in range(C):
            if graph[i][j] != '.':
                graph[i][j] = 'O'
# 첫 1초는 0만 1로 변경해준다.
for i in range(R):
    for j in range(C):
        if graph[i][j] != '.':
            graph[i][j] = 1
for i in range(2, N+1):
    bomb_list = time_pass()
    # 제거할 폭탄이 있으면 차례로 터뜨린다.
    
    while bomb_list:
        r, c = bomb_list.pop()
        bomb(r,c)

to_zero()
for i in range(R):
    print("".join(graph[i]))