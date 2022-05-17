N = int(input())
board = []
output = []
for i in range(N):
    row = list(map(int, input().split()))
    board.append(row)
def find_paper(board,r,c,n):
    if n==1:
        return board[r][c]
    # n의 크기에 색이 같은지 확인
    # 같지 않으면 //3
    prev = board[r][c]
    is_fail=0
    for i in range(r,r+n):
        for j in range(c,c+n):
            if prev != board[i][j]:
                is_fail=1
                break
        if is_fail ==1:
            break
    if is_fail==1:
        slice_n = n//3
        output.append(find_paper(board,r,c,slice_n))
        output.append(find_paper(board,r+slice_n,c,slice_n))
        output.append(find_paper(board,r+slice_n+slice_n,c,slice_n))
        output.append(find_paper(board,r,c+slice_n,slice_n))
        output.append(find_paper(board,r,c+slice_n+slice_n,slice_n))
        output.append(find_paper(board,r+slice_n, c+slice_n, slice_n))
        output.append(find_paper(board,r + slice_n + slice_n,c + slice_n,slice_n))
        output.append(find_paper(board,r + slice_n,c + slice_n + slice_n,slice_n))
        output.append(find_paper(board,r + slice_n + slice_n,c + slice_n + slice_n,slice_n))
    else:
        return board[r][c]
output.append(find_paper(board,0,0,N))
a = 0
b = 0
c = 0
for i in range(len(output)):
    if output[i] == -1:
        a+=1
    elif output[i] == 0:
        b+=1
    elif output[i] == 1:
        c+=1
print(a)
print(b)
print(c)