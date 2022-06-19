# 17299
N = int(input())
numbers = list(map(int, input().split()))
count = [0]* (max(numbers))
result = [-1] * len(numbers)
stack = []
stack.append(0)
# i번째가 
for i in numbers:
    count[i-1] += 1

for i in range(1, len(numbers)):
    while stack and numbers[stack[-1]] != numbers[i] and count[numbers[stack[-1]]-1] < count[numbers[i]-1]:
        result[stack.pop()] = numbers[i]
    stack.append(i)
print(*result)
