A, B = map(int, input().split())

answer = 1e9
def dfs(val, cnt):
    global answer
    if val >= B:
        if val == B:
            answer = min(cnt, answer)
        #print(val)
        return
    # 
    dfs(val*2, cnt+1)
    #
    dfs(int(str(val) + '1'), cnt+1)

dfs(A,1)
if answer == 1e9:
    print(-1)
else:
    print(answer)