N, M = map(int, input().split())
num = sorted(list(map(int, input().split())))
setted_num = sorted(list(set(num)))
stack = []
def permu():
    if len(stack) == M:
        print(*stack)
        return
    for i in range(len(setted_num)):
        stack.append(setted_num[i])
        permu()
        stack.pop()
permu()