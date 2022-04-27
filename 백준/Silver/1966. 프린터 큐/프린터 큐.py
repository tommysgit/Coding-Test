testCase = int(input())
orders = []
targets = []
for testCase in range(testCase):
    N, index = map(int, input().split()) # N개의 리스트 속 개수와 찾고자 하는 M번째 인덱스
    order = [int(N) for N in input().split()]
    length = len(order)
    i = 0
    target = order[index] # 목표로하는 값
    targetOrder = 0
    while i < length-1: # i에 대한 검증 j를 돌면서 i보다 큰 수가 나오면 i를 리스트의 끝으로 보내고
        j = i+1 
        while j < length:
            if order[i] < order[j]: # i번째 자리 수보다 큰 수 발견시 i번째 수는 맨 뒤로 가고 i+1의 자리가 i번째 자리로 간다.
                # 맨 처음 선택한 인덱스의 값은 
                #타겟이 0번 혹은 i번째면 length - 1 로가도록 하고 타겟이 제 자리일경우
                if index == i or index == 0: # index가 
                    index = len(order) - 1
                elif index<i:
                    index = index
                else:
                    index = index - 1
                tmp = order[i]
                del order[i]
                order.append(tmp)
                j = i+1
                continue
            j = j+1
        if index ==i: # 이거 때문에 삽질함 i번째에 index가 자기 자리 찾을경우 그만돌아야함
            break
        i = i +1
    targets.append(index + 1)
    orders.append(order)
for i in targets:
    print(i)   