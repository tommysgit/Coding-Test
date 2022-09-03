import itertools
def solution(number):
    answer = 0
    # 배열 중 3개의 수의합이 0이되는 개수를 반환
    for nums in itertools.combinations(number, 3):
        if sum(nums) == 0:
            answer += 1
    return answer