# 1406
import sys

strings1 = list(input())
strings2 = []
count = int(input())
for i in range(count):
    command = list(map(str, sys.stdin.readline().split()))
    if command[0] == 'L':
        if strings1:
            strings2.append(strings1.pop())
    elif command[0] == 'D':
        if strings2:
            strings1.append(strings2.pop())
    elif command[0] == 'B':
        if strings1:
            strings1.pop()
    else:
        strings1.append(command[1])
strings1.extend(reversed(strings2))
print("".join(strings1))