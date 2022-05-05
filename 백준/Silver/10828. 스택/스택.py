from collections import deque

N = int(input())
prints = []
stack = deque()
for i in range(N):
    command = str(input())
    if 'push' in command:
        command, num = command.split()
        stack.append(int(num))
    elif command == 'pop':
        if len(stack)>0:
            prints.append(stack.pop())
        else:
            prints.append(-1)
    elif command == 'size':
        prints.append(len(stack))
    elif command == 'empty':
        if len(stack) == 0:
            prints.append(1)
        else:
            prints.append(0)
    elif command == 'top':
        if len(stack) == 0:
            prints.append(-1)
        else:
            prints.append(stack[len(stack)-1])
    else:
        print('error')
for i in prints:
    print(i)