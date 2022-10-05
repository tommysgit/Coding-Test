from collections import deque


n, m = map(int, input().split())
q_cor, k_cor, p_cor = [],[],[]
q_list = list(map(int, input().split()))
k_list = list(map(int, input().split()))
p_list = list(map(int, input().split()))
k_cnt, q_cnt, p_cnt = k_list[0], q_list[0], p_list[0]
k_list, q_list, p_list = k_list[1:], q_list[1:], p_list[1:]
board = [['0' for c in range(m)] for r in range(n)]
for i in range(0, q_cnt*2, 2):
    q_cor.append((q_list[i]-1, q_list[i+1]-1))
    board[q_list[i]-1][q_list[i+1]-1] = 'q'
for i in range(0, k_cnt*2, 2):
    k_cor.append((k_list[i]-1, k_list[i+1]-1))
    board[k_list[i]-1][k_list[i+1]-1] = 'k'
for i in range(0, p_cnt*2, 2):
    p_cor.append((p_list[i]-1, p_list[i+1]-1))
    board[p_list[i]-1][p_list[i+1]-1] = 'p'
# q는 가로, 세로, 대각선 장애물이 없으면 끝까지 갈 수 있음
# k는 한칸 직진 후 대각선
# p는 장애물
kr = [1, 1, -1, -1, 2, 2, -2, -2]
kc = [-2, 2, -2, 2, -1, 1, -1, 1]
qr = [-1, 1, 0, 0, -1, -1, 1, 1]
qc = [0, 0, -1, 1, -1, 1, -1, 1]
case = ['p', 'q', 'k']
for r in range(n):
    for c in range(m):
        if board[r][c] == 'q':
            for i in range(8):
                mr ,mc = r + qr[i], c + qc[i]
                if 0 <= mr < n and 0 <= mc < m and board[mr][mc] not in case:
                    q = deque([])
                    q.append((mr,mc))
                    board[mr][mc] = '1'
                    while q:
                        tmp_r, tmp_c = q.popleft()
                        mr, mc =  tmp_r + qr[i], tmp_c + qc[i]
                        if 0 <= mr < n and 0 <= mc < m and board[mr][mc] not in case:
                            q.append((mr,mc))
                            board[mr][mc] = '1'
        elif board[r][c] == 'k':
            for i in range(8):
                mr , mc = r + kr[i], c + kc[i]
                if 0 <= mr < n and 0 <= mc < m and board[mr][mc] not in case:
                    board[mr][mc] = '1'
ans = 0
for r in range(n):
    for c in range(m):
        if board[r][c] == '0':
            ans += 1
print(ans)