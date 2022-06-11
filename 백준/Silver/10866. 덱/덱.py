from collections import deque
import sys


N = int(input())
queue = deque()
result = []
for i in range(N):
    command = list(sys.stdin.readline().split())
    if command[0] == "push_front":
        queue.appendleft(command[1])
    elif command[0] == "push_back":
        queue.append(command[1])
    elif command[0] == "pop_front":
        if queue:
            result.append(queue.popleft())
        else:
            result.append(-1)
    elif command[0] == "pop_back":
        if queue:
            result.append(queue.pop())
        else:
            result.append(-1)
    elif command[0] == "size":
        result.append(len(queue))
    elif command[0] == "empty":
        if len(queue) == 0:
            result.append(1)
        else:
            result.append(0)
    elif command[0] == "front":
        if queue:
            result.append(queue[0])
        else:
            result.append(-1)
    else:
        if queue:
            result.append(queue[len(queue)-1])
        else:
            result.append(-1)
for i in result:
    print(i)