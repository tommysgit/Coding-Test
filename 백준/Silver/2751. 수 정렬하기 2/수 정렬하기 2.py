import sys
numbers = [int(sys.stdin.readline().rstrip()) for i in range(int(input()))]
numbers.sort()
for i in numbers:
    print(i)