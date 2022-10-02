import re
import sys

N = int(input())
serial_set = []
for i in range(N):
    serial = sys.stdin.readline().strip()
    serial_set.append(serial)
serial_set.sort(key= lambda x : [len(x), sum(list(map(int, re.sub('[A-Z]', '', x)))), x])
for serial in serial_set:
    print(serial)