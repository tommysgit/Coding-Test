from copy import deepcopy


N, M = map(int, input().split())
num = sorted(list(map(int, input().split())))
sorted_num = sorted(list(set(num)))
visited = [0] *(max(num)+1)
stack =[]
result = []
def permu(start):
    #print(stack, start )
    if len(stack) == M:
        if stack not in result:
            result.append(deepcopy(stack))
        return
    for i in range(start, len(num)):
        #print(i, start)
        
        if num.count(num[i]) > visited[num[i]]:
            stack.append(num[i])
            visited[num[i]] +=1
            permu(i+1)
            visited[num[i]] -=1
            stack.pop()
permu(0)
for i in result:
    print(*i)
