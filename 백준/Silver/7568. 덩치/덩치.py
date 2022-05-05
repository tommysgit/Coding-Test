N = int(input())
lists = [list(map(int, input().split()))for i in range(N)]
isOrdered = [False]*(len(lists)+1)
order = [0]*(len(lists))
# 2차원 배열을 순회하면서 자기보다 큰 수가 몇개인지 찾는다.
for i in range(len(lists)):
    tmp = lists[i]
    count = 0
    for j in range(len(lists)):
        if tmp == list[j]:
            continue
        if lists[j][0]>tmp[0] and lists[j][1]>tmp[1]:
            count += 1
    order[i] = count+1
for i in range(len(order)):
    print(order[i], end = ' ')