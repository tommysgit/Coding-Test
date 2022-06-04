# 10972
import sys
sys.setrecursionlimit(1000000)
N = int(input())
target = list(map(int, sys.stdin.readline().split()))
def permu(num):
    for i in reversed(range(len(num))):
        if num[i] > num[i-1]:
            x = i-1 # 1
            y = i # 4
            # 2 1 4 3
            for j in reversed(range(len(num))):
                if num[j] > num[x]:

                    num[j], num[x] = num[x], num[j] # 2 3 4 1
                    num = num[:y] + sorted(num[y:])
                    print(*num)
                    exit()

reversed_num = list(reversed(list(range(1,N+1))))
if target == reversed_num:
    print(-1)
else:
    permu(target)