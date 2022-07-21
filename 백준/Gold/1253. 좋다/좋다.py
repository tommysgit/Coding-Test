import sys
import bisect

# 숫자의 개수
N = int(input())
# N개의 수
A = list(map(int, sys.stdin.readline().strip().split()))
A.sort()
count = 0
# 다른 두 개의 인덱스 값의 합이 있으면 카운트
# left는 작은 수 right는 큰 수
# 정렬한 뒤 i번째 인덱스 전까지 이진탐색으로 푼다.
def binary_search(i):
    target = A[i]
    left = 0
    right = N-1
    if i == left:
        left += 1
    if i == right:
        right -= 1
    # left인덱스와 right인덱스의 합을 구하고 타겟과 크기를 비교하여 값이 작으면 left증가 크면 right 감소
    while left < right:
        
        two_sum = A[left] + A[right]
        if two_sum < target:
            left += 1
        elif two_sum > target:
            right -= 1
        else:
            return 1
        if i == left:
            left += 1
        if i == right:
            right -= 1
    return 0
# 
tmp = []
for i in range(N):
    result = binary_search(i)
    if result:
        count += 1
        #tmp.append(i)
print(count)