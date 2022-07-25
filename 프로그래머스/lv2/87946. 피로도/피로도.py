def solution(k, dungeons):
    global answer
    answer = -1
    is_visit = [0]*len(dungeons)
    # 백트래킹 순열 이용?
    def dfs(val, cnt):
        global answer
        answer = max(answer, cnt)
        for i in range(len(dungeons)):
            min_cost, cost = dungeons[i]
            if val>= min_cost:
                if not is_visit[i]:
                    is_visit[i] = 1
                    dfs(val - cost, cnt+1)
                    is_visit[i] = 0
    dfs(k, 0)
    return answer