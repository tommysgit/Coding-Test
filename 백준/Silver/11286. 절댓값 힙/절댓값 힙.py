# 11286

from sys import stdin
N = int(input())
heap = []
tmp = []
def heapify(heap, index):
    child_index = index
    while child_index !=0 : # 0이면 빠져나온다.
        parent_index = (child_index - 1) // 2
        # 절대 값 양수 음수 비교 -> 절대 값이 작고 음수인 수가 위 혹은 왼쪽으로
        if abs(heap[parent_index]) > abs(heap[child_index]) or (abs(heap[parent_index]) == abs(heap[child_index]) and heap[child_index]< heap[parent_index]):
            heap[parent_index], heap[child_index] = heap[child_index], heap[parent_index]
            child_index = parent_index
        else:
            return
def find_bigger_child(index, heap_size):
    parent = index
    left_child = index*2 + 1
    right_child = index*2 + 2
    
    # 왼쪽 자식과 비교
    if left_child<heap_size :
        if abs(heap[left_child]) < abs(heap[parent]) or (abs(heap[left_child]) == abs(heap[parent]) and heap[left_child] < heap[parent]):
            parent = left_child
    if right_child<heap_size :
        if abs(heap[right_child]) < abs(heap[parent]) or (abs(heap[right_child]) == abs(heap[parent]) and heap[right_child] < heap[parent]):
            parent = right_child
    return parent
def down_heapify(heap, index):
    parent_idex = index
    bigger_child_index = find_bigger_child(index, len(heap))
    while parent_idex != bigger_child_index:
        heap[bigger_child_index], heap[parent_idex] = heap[parent_idex], heap[bigger_child_index]
        parent_idex = bigger_child_index
        bigger_child_index = find_bigger_child(bigger_child_index, len(heap))
    
        
for i in range(N): # X가 0이면 배열에서 절대값이 작은 값을 출력하고 제거 아니면 삽입
    # 절대값 비교 후 음수 양수 비교
    tmp.append(int(stdin.readline()))

for i in range(N):
    X = tmp[i]
    if X == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heap[0])
            heap[0], heap[len(heap)-1] = heap[len(heap)-1], heap[0]
            del heap[len(heap)-1]
            if len(heap)>1:
                down_heapify(heap, 0) 
        
    else :
        heap.append(X)
        heapify(heap, len(heap)-1)
        

