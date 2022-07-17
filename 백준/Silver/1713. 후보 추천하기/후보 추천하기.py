import heapq


N = int(input())
students = int(input())
recommend_list = list(map(int, input().split()))
# recommend_hash = {}
#photo = []
heap = []
# 힙의 학생 인덱스를 반환
def search_student(num):
    for i in range(len(heap)):
        recommend, idx, student = heap[i]
        if num == student:
            return i
    return -1

for i in range(len(recommend_list)):

    # 우선순위 큐에 삽입시 학생번호, 추천수, i번째 인덱스를 삽입한다.
    # mean_heap 
    # 추천 수는 낮고 먼저 들어온 값이 우선순위
    student_idx = search_student(recommend_list[i])
    # 이미 사진틀에 있을 경우 추천수만 올려준다.
    if student_idx != -1:
        recommend, idx, student = heap[student_idx]
        del heap[student_idx]
        heapq.heapify(heap)
        heapq.heappush(heap, (recommend+1, idx, student))
        
    # 사진관에 없으면 우선순위 높은 것 빼고 새로 삽입
    else:
        # 사진틀이 다 찼으면 우선순위 높은 것 하나 제거
        if len(heap) == N:
            heapq.heappop(heap)
        heapq.heappush(heap, (1, i, recommend_list[i]))
result = sorted(heap, key= lambda x: x[2])
for i in result:
    print(i[2], end=' ')