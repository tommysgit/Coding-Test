from collections import deque
N = int(input())
coms = []
nums = []
queue = deque()
content = []
for i in range(N):
    command = str(input())
    if 'push' in command:
        command, num = command.split()
    # coms.append(command)
    # nums.append(num)
    if command == 'push':
        queue.append(num)
    elif command == 'pop':
        if len(queue)>0:
            content.append(queue.popleft())
        else:
            content.append(-1)
    elif command == 'size':
        content.append(len(queue))
    elif command == 'empty':
        if len(queue) == 0:
            content.append(1)
        else:
            content.append(0)
    elif command == 'front':
        if len(queue)>0:
            content.append(queue[0])
        else:
            content.append(-1)
    elif command == 'back':
        if len(queue)>0:
            content.append(queue[len(queue)-1])
        else:
            content.append(-1)
    else:
        print('error')
for i in range(len(content)):
    print(content[i])