# 9012
T = int(input())
def check_bracket(brackets):
    stack = []
    is_bracket = 1
    for i in range(len(brackets)):
        if brackets[i] == '(':
            stack.append(brackets[i])
        else:
            if len(stack) == 0:
                is_bracket = 0
                break
            tmp = stack.pop()
            if tmp != '(':
                is_bracket = 0
                break
        
    if is_bracket == 1 and len(stack) == 0:
        result.append('YES')
    else:
        result.append('NO')


result = []
for i in range(T):
    brackets = input()
    check_bracket(brackets)
for i in result:
    print(i)