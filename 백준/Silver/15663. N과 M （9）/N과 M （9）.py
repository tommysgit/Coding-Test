from copy import deepcopy
import sys
sys.setrecursionlimit(100000)
N, M = map(int, input().split())
num = sorted(list(map(int, input().split())))
sorted_num = sorted(list(set(num)))
visited = [0]*((len(sorted_num))+1)
stack = []
result = []
def permu():
    if len(stack) == M:
        if stack not in result:
            result.append(deepcopy(stack))
        return
    # 중복 숫자가 있으면 중복 숫자만큼 수를 써야한다.
    for i in range(len(sorted_num)):
        if visited[i]< num.count(sorted_num[i]):
            stack.append(sorted_num[i])
            visited[i] +=1
            permu()
            stack.pop()
            visited[i] -= 1

permu()
for i in result:
    print(*i)