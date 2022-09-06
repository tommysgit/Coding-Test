class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]
        is_visit = [[0 for col in range(n)] for row in range(m)]
        answer = []
        # 우 하 좌 상
        def dfs(r,c, d):
            is_visit[r][c] = 1
            answer.append(matrix[r][c])
            for i in range(2):
                d = (d+i)%4
                mr = r + dr[d]
                mc = c + dc[d]
                if 0<=mr<m and 0<=mc<n and not is_visit[mr][mc]:
                    dfs(mr,mc,d)
                    break
        dfs(0,0,0)
        return answer
            