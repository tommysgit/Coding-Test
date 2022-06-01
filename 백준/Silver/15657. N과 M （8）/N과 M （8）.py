N, M = map(int, input().split())
num = sorted(list(map(int, input().split())))
stack = []
def permu(start):
    if len(stack) == M:
        print(*stack)
        return
    for i in range(start, len(num)):
        stack.append(num[i])
        permu(i)
        stack.pop()
permu(0)