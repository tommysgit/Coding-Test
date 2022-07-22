import heapq
import sys

# 거인의 수, 센티의 키, 뿅망치 사용가능 횟수
N, H, T = map(int, input().split())
tall_list = []
for i in range(N):
    tall = int(sys.stdin.readline().strip())
    heapq.heappush(tall_list, (-tall, tall))
count = 0
while 1:
    # 뿅망치 다 사용한 경우 탈출
    if count == T:
        break
    # 가장 큰 키 pop
    tall = heapq.heappop(tall_list)[1]
    # 거인의 키가 크거나 같고 1이 아닌경우
    # 거인의 키가 1이면 뿅망치가 먹지 않는다.
    if tall >= H and tall != 1:
        # 뿅망치 사용
        count += 1
        tall = tall//2
        # 키 리스트에 삽입
        heapq.heappush(tall_list, (-tall, tall))
    # 센티가 더 큰 경우
    else:
        # 뿅망치 사용하지 않고 그냥 삽입하고 탈출
        heapq.heappush(tall_list, (-tall, tall))
        break
if tall_list[0][1] >= H:
    print("NO")
    print(tall_list[0][1])
else:
    print("YES")
    print(count)