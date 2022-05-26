E, S, M = map(int, input().split())
year = 1
tmp1 = tmp2 = tmp3 = 1
while True:
    if tmp1 == E and tmp2 == S and tmp3 == M:
        print(year)
        break
    year +=1
    tmp1 +=1
    tmp2 +=1
    tmp3 +=1
    if tmp1>15:
        tmp1 = 1
    if tmp2>28:
        tmp2 = 1
    if tmp3>19:
        tmp3 = 1