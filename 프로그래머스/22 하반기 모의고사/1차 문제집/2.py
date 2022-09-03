def solution(topping):
    answer = 0
    max_num = max(topping)
    arr = [0]*(max_num+1)
    sets = set([])
    left = len(set(topping))
    right = 0
    # 토핑의 개수를 채운다.
    for i in range(len(topping)):
        arr[topping[i]] += 1
    for i in reversed(range(len(topping))):
        if topping[i] not in sets:
            sets.add(topping[i])
            right += 1
        arr[topping[i]] -= 1
        if arr[topping[i]] == 0:
            left -= 1
        if left == right:
            answer += 1
        # print(arr, sets)
        # print(left, right)
    return answer