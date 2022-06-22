import sys
N, M = map(int, input().split())
trees = list(map(int, sys.stdin.readline().split()))
# 길이를 이분탐색으로, mid가 낮아질수록 더 잘라야하고 높아질수록 덜 잘라야한다 1 20 / 11 20 / 12 20 / 12 19
def binary_sort(trees, left, right, target):
    while left <= right:
        mid = (left + right)//2 # 10 15 16
        
        sum = 0
        # 배열을 돌면서 mid 보다 큰 나무를 자른 값의 합을 구한다.
        for i in trees: 
            if i > mid:
                sum += i-mid
        # sum이 target보다 같거나 크면 필요한 target보다 많이 잘랐으므로 mid를 left로 바꿔 다시 반복문
        if sum >= target:
            left = mid+1
        # sum이 target보다 덜 잘랐으므로 mid의 right는 볼 필요가 없다.
        else:
            right = mid -1
    return right
output = binary_sort(trees, 1, max(trees), M)
print(output)