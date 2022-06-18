import sys


N = int(input())
result = [-1] * N
numbers = list(map(int, sys.stdin.readline().split()))
stack = []
stack.append(0)
# i를 돌면서 오큰수를 찾지 못한 인덱스는 스택으로
for i in range(1, N):
    while stack and numbers[stack[-1]] < numbers[i]:
        result[stack.pop()] = numbers[i]
    stack.append(i)
print(*result)