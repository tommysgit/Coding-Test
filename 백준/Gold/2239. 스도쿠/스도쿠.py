board = []
empty = []
for i in range(9):
    tmp = list(map(int, input()))
    board.append(tmp)
    for j in range(9):
        if tmp[j] == 0:
            empty.append((i,j))
def check_num(r, c, num):
    # row check
    # col check
    for i in range(9):
        if board[r][i] == num or board[i][c] == num:
            return False
    # square check\
    start_r, start_c = r//3 , c//3
    for i in range(3):
        for j in range(3):
            if board[3*start_r+i][3*start_c+j] == num:
                return False
    return True

# 백트래킹
# empty에 있는 좌표가 행,열,사각형 범위에 들어갈 수 있는지 확인
def back_track(depth):
    if depth == len(empty):
        for r in range(9):
            for c in range(9):
                print(str(board[r][c]), end="")
            print()
        exit()
    r, c = empty[depth]
    origin = board[r][c]
    for num in range(1, 10):
        if check_num(r, c, num):
            board[r][c] = num
            back_track(depth + 1)
            board[r][c] = origin
back_track(0)