N = int(input())
target = list(map(int, input().split()))
def find_min(num):
    for i in reversed(range(N)):
        if num[i] < num[i-1]:
            # 2 1 3 4 -> 1 4 3 2
            x = i-1 # 2
            y = i # 1
            for j in reversed(range(N)):
                if num[j] < num[x]:
                    num[x], num[j] = num[j], num[x]
                    num = num[:y] + list(reversed(sorted(num[y:])))
                    print(*num)
                    exit()
if list(range(1,N+1)) == target:
    print(-1)
else:
    find_min(target)