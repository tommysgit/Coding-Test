from copy import deepcopy


N, M = map(int, input().split())
num = sorted(list(map(int, input().split())))
sorted_num = sorted(list(set(num)))
stack = []
result = []
visited = [0]* (max(sorted_num)+1)
def permu(start):

    if len(stack) == M:
        if stack not in result:
            result.append(deepcopy(stack))
        return
    
    for i in range(start, len(sorted_num)):
        
        stack.append(sorted_num[i])
        permu(i)
        stack.pop()
# for i in range(len(sorted_num)):
#     permu(i)

permu(0)
for i in result:
    print(*i)