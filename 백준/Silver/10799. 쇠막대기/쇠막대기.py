brackets = input()
stack = []
count = 0
for i in range(len(brackets)):
    if brackets[i] == '(':
        stack.append(brackets[i])
    else:
        if brackets[i-1] == '(': # 레이저인 경우
            stack.pop()
            count += len(stack)
        else: # 막대기인 경우
            stack.pop()
            count += 1
print(count)