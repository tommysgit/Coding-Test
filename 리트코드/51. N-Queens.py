from copy import deepcopy
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        answer = []
        std_board = []
        visit = [-1]*n
        for i in range(n):
            line = []
            for j in range(n):
                line.append(".")
            std_board.append(line)
        # [1, 3, 0, 2] [0, 2, 1, 3]
        # 해당 퀸이 잡을 수 있는지
        def check(nth_row):
            # 세로 대각선 확인
            for row in range(nth_row):
                
                if visit[row] == visit[nth_row] or nth_row - row == abs(visit[nth_row] - visit[row]):
                    return False
            return True
        def dfs(row):
            if row == n:
                tmp_board = []
                for i in range(n):
                    tmp_str = ""
                    for j in range(n):
                        if visit[i] == j:
                            tmp_str += "Q"
                        else:
                            tmp_str += "."
                    tmp_board.append(tmp_str)
                answer.append(tmp_board)
                return
            
            # 1~n행을 돌며 열을 확인
            for col in range(n):
                visit[row] = col
                # 해당 row와 col에 퀸을 두었을 때 다음 열에 잡히지않는 퀸이 있으면 진행
                if check(row):
                    dfs(row+1)
        
        dfs(0)
        # print(answer)
        return answer