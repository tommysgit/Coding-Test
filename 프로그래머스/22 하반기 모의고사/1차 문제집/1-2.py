from collections import Counter
def solution(want, number, discount):
    answer = 0
    for i in range(len(discount) - 9):
        counter_hash = Counter(discount[i:i+10])
        is_success = 1
        for j in range(len(want)):
            product = want[j]
            num = number[j]
            # 존재하지 않거나 충족이 안되면 탈출
            if product not in counter_hash or counter_hash[product] < num:
                is_success = 0
                break
        if is_success:
            answer += 1
    return answer