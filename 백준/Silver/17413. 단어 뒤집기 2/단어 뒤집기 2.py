strings = input()
stack = []
result = []
is_bracket = 0
# 괄호를 만나거나 띄어쓰기가 있거나 마지막인경우 스택을 비운다.
for i in range(len(strings)):
    if strings[i] == '<':
        is_bracket = 1
        while stack:
            result.append(stack.pop())
        stack.append(strings[i])
    elif strings[i] == '>':
        is_bracket = 0
        stack.append(strings[i])
        while stack:
            result.append(stack[0])
            del stack[0]
    elif is_bracket == 0 and strings[i] == ' ':
        while stack:
            result.append(stack.pop())
        result.append(' ')
    else:
        stack.append(strings[i])
        if i == len(strings) - 1:
            while stack:
                result.append(stack.pop())
    
print(''.join(s for s in result))