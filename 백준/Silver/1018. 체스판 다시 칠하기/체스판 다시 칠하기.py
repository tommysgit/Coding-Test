import sys
sys.setrecursionlimit(2500)
N, M = map(int, input().split())
board = []
min_list = []
for i in range(N):
    row = str(input())
    board.append(row)
def slice_board(board, start_row, start_col, min_list):
    # 더이상 자를 수 없으면 반환
    sliced_board = []
    rev = []
    if  start_col+8>N:
        return
    # start_row , start_col을 기준으로 8x8 보드판을 만든다.
    for i in range(start_col, start_col+8):
        sliced_board.append(board[i][start_row: start_row+8])
    # 자른 보드판의 최소로 칠해야하는 정사각형의 개수를 구한다.
    for i in range(len(sliced_board)):
        rev.append(sliced_board[i][::-1])

    min_list.append(min_square(sliced_board))
    min_list.append(min_square(sliced_board[::-1]))
    min_list.append(min_square(rev))

    # row를 증가하여 다시 자른다.
    if start_row+9>M:
        slice_board(board, 0, start_col+1, min_list)
    else:
        slice_board(board, start_row+1, start_col, min_list)
def min_square(slice_board):
    W = 'W'
    B = 'B'
    b_min = 0
    w_min = 0
    # 검정 시작은 짝수열 짝수행, 홀수열 홀수행은 B / 짝수열 홀수행, 홀수열 짝수행은 W
    if slice_board[0][0] == B:
        for i in range(len(slice_board)):
            for j in range(len(slice_board[i])):
                if (((i%2 == 0 and j%2==0) or (i%2!=0 and j%2 !=0)) and slice_board[i][j] !=B):
                    b_min +=1
                elif(((i%2 == 0 and j%2!=0) or (i%2!=0 and j%2 ==0)) and slice_board[i][j] !=W):
                    b_min +=1
        return b_min
    # 흰 시작은 짝수열 짝수행, 홀수열 홀수행은 W / 짝수열 홀수행, 홀수열 짝수행은 B
    else:
        for i in range(len(slice_board)):
            for j in range(len(slice_board[i])):
                if (((i%2 == 0 and j%2==0) or (i%2!=0 and j%2 !=0)) and slice_board[i][j] !=W):
                    w_min +=1
                elif(((i%2 == 0 and j%2!=0) or (i%2!=0 and j%2 ==0)) and slice_board[i][j] !=B):
                    w_min +=1
        return w_min

slice_board(board, 0, 0, min_list)
print(min(min_list))