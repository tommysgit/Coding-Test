# 2110
import sys


N, C = map(int, input().split())
lists = []
fix = []
for i in range(N):
    lists.append(int(sys.stdin.readline()))

lists.sort()
# fix.append(lists[0])
# fix.append(lists[-1])


def binary_search(start, end):

    # 이진 탐색으로 최소 거리와 최대 거리 사이에서 찾아야한다.
    # 1 2 4 8 9
    # 1 , 3 -> mid = 2 / 3, 3 -> mid = 3
    
    result = 0
    while start <= end:
        start_house = lists[0]
        mid = (start + end) // 2
        predict = 1
        for i in range(1, N):
            if lists[i] >= start_house + mid:
                #print(start_house, lists[i])
                predict += 1
                start_house = lists[i]

                
            # mid의 거리보다 큰 집들이 와이파이 수보다 많으면 탈출
            if predict > C:
                break
        # 거리가 많다고 여겨지면 시작점을 뒤로 하여 더 큰 거리를
        #print('test', start, end, mid, predict, result)
        if predict >= C:
            start = mid + 1
            result = mid
        
        if predict < C:
            end = mid - 1
    return result
print(binary_search(1, lists[-1]-lists[0]))