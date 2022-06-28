# 2512
N = int(input())
input_list = list(map(int, input().split()))
M = int(input())
input_list.sort()
input_sum = sum(input_list)
#input_avg = (input_sum) // N

# 이진 탐색으로 평균보다 큰 값과 개수를 구한다.
def binary_search(left, right):
    result = 0
    while left <= right:
        mid =(left + right) // 2
        idx = 0
        for i in range(len(input_list)):
            if input_list[i]> mid:
                idx = i
                break
        tmp_sum = sum(input_list[:idx]) + (mid*(len(input_list[idx:])))
        if tmp_sum <= M:
            left = mid + 1
            result = mid
        else:
            right = mid - 1
    return result

if input_sum > M:
    large_input = binary_search(0, max(input_list))
    print(large_input)
else:
    print(max(input_list))   
