from collections import deque
def solution(rows, columns, queries):
    graph = [[0 for c in range(columns)] for r in range(rows)]
    dr = [0, 1, 0 ,-1]
    dc = [1, 0, -1, 0]
    num = 1
    answer = []
        
    for r in range(rows):
        for c in range(columns):
            graph[r][c] = num
            num += 1
    for r1, c1, r2, c2  in queries:
        r1, c1, r2, c2 = r1 - 1, c1 - 1, r2 -1, c2-1
        std = [(r1,c2), (r2,c2), (r2,c1), (r1,c1)]
        sr, sc, pr, pc = r1,c1, r1, c1
        num = 1e9
        tmp = deque([])
        tmp.append(graph[r1][c1])
        for i in range(4):
            while (sr,sc) != std[i]:
                
                pr,pc = sr, sc
                
                sr,sc = sr + dr[i], sc + dc[i]
                tmp.append(graph[sr][sc])
                v = tmp.popleft()
                num = min(v, num)
                #print(sr, sc, v)
                graph[sr][sc] = v
                #print(sr,sc)
                #graph[sr][sc] = tmp.popleft()
            
        # for i in range(len(graph)):
        #     print(*graph[i])
        # print(tmp)
        answer.append(num)
        
    
    return answer