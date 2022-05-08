import sys
N, M = map(int, sys.stdin.readline().split())
site_list = {}
find_site = []
for i in range(N):
    key, value = map(str, input().split())
    site_list[key] = value
for i in range(M):
    find_site.append(str(input()))

for i in range(M):
    site = find_site[i]
    print(site_list.get(site))