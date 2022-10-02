from collections import deque
from copy import deepcopy

A, B, C = map(int, input().split())
bucket = (A,B,C)
def bfs():
    first = ['0','0',str(C)]
    q = deque([])
    q.append([[0,0,C], 2])
    tmp_set = set()
    tmp_set.add(' '.join(first))
    ans = set()
    while q:
        cur_bucket , turn = q.popleft()
        #print(cur_bucket, turn)
        if cur_bucket[0] == 0:
            ans.add(cur_bucket[2])
        for i in range(3):
            if turn == i:
                continue
            tmp_arr = deepcopy(cur_bucket)
            # bucket[i]를 가득 채우거나 turn을 비울때까지 물을 준다.
            # 넣을 수 있는 물의 양
            tmp = bucket[i] - cur_bucket[i]
            # 물을 다 줄 수 있으면 주고 
            if cur_bucket[turn] >= tmp:
                tmp_arr[i] = bucket[i]
                tmp_arr[turn] -= tmp
                
            # 물을 비울때까지 준다.
            else:
                tmp_arr[i] += cur_bucket[turn]
                tmp_arr[turn] = 0
            test = ' '.join(list(map(str, tmp_arr)))
            if test not in tmp_set:
                for j in range(3):
                    q.append([tmp_arr, j])
                tmp_set.add(test)    
    ans = list(ans)
    ans.sort()
    print(*ans)
bfs()