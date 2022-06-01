N, M = map(int, input().split())
num = sorted(list(map(int, input().split())))
stack = []
def permu():
    if len(stack) == M:
        print(*stack)
        return
    for i in range(len(num)):
        stack.append(num[i])
        permu()
        stack.pop()
permu()