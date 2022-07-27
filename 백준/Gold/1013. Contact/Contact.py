import re
T = int(input())
# (1001+1+ | 01)+
for i in range(T):
    num = input()
    t = re.compile('(100+1+|01)+')
    if t.fullmatch(num):
        print("YES")
    else:
        print("NO")