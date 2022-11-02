from itertools import combinations


N, S = map(int, input().split())
nums = list(map(int, input().split()))
cnt = 0
for i in range(1, N+1):
    for combi in combinations(nums, i):
        if sum(combi) == S:
            cnt += 1
print(cnt)