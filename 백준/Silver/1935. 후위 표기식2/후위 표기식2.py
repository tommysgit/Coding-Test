import re
N = int(input())
is_upper = re.compile("[A-Z]")
notation = input()
stack = []
num = [0]*N
# 정규식으로 후위식에 문자들의 수만큼
for i in range(N):
    num[i] = int(input())
for i in notation:
    if is_upper.findall(i):
        stack.append(num[ord(i)-65])
    else:
        a = stack.pop()
        b = stack.pop()
        if i == '/':
            output = b/a
        if i == '*':
            output = b*a
        if i == '+':
            output = b+a
        if i == '-':
            output = b-a
        stack.append(output)
print(format(stack[0], '.2f'))