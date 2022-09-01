# 14499

N, M, x,y,K = map(int, input().split())
graph = [list(map(int, input().split())) for i in range(N)]
order = list(map(int, input().split()))
dr = [0, 0, 0, -1, 1]
dc = [0, 1, -1, 0, 0]
cur = (x,y)
dice = [0,0,0,0,0,0,0]
def turn(dir, dice):
    # 주사위는 고정되어 있고 숫자만 바뀐다고 치자
    x, a,b,c,d,e, f = dice
    # 동
    if dir == 1:
        dice = [x, c, b,f, a, e, d]
        
    # 서
    elif dir == 2:
        dice = [x ,d, b, a, f,e, c]
        
    # 북
    elif dir == 3:
        dice = [x, b, f, c,d,a, e]
        
    # 남
    else:
        dice = [x, e, a, c,d, f, b]
        
    return dice
for num in order:
    x, y = cur
    dx = x + dr[num]
    dy = y + dc[num]
    if dx <0 or dy < 0 or dx>= N or dy >= M:
        continue
    cur = (dx, dy)
    dice = turn(num, dice)
    if graph[dx][dy] == 0:
        graph[dx][dy] = dice[1]
    else:
        dice[1] = graph[dx][dy]
        graph[dx][dy] = 0

    print(dice[6])

    