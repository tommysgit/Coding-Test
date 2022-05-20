import sys


N , M = map(int, input().split())
hash_map = dict()
output = []
for i in range(N):
    hash_map[sys.stdin.readline().strip()] = 1
for i in range(M):
    tmp2 = sys.stdin.readline().strip()
    if tmp2 in hash_map:
        output.append(tmp2)
print(len(output))
output.sort()
for i in output:
    print(i)