N, M = map(int, input().split())
num = sorted(list(map(int, input().split())))
visited = [False]*N
stack = []
def permu(start):
    if len(stack) == M:
        print(*stack)
        return 
    for i in range(start,N):
        if num[i] not in stack :
            stack.append(num[i])
            permu(i+1)
            stack.pop()
permu(0)