import itertools
def solution(orders, course):
    answer = []
    order_hash = {}
    # 단품 메뉴의 코스 조합을 모두 구하여 카운트
    for i in range(len(orders)):
        for j in course:
            # j개의 조합을 선택하여 해시에 삽입
            for case in itertools.combinations(orders[i], j):
                # case를 자음순으로 정렬해야 같은 코스로 인식한다.
                case = ''.join(case)
                case = ''.join(sorted(case))
                if not order_hash.get(case):
                    order_hash[case] = 0
                order_hash[case] += 1
    # 코스의 개수는 오름 차순, 중복 코스는 내림 차순으로 정렬
    list_hash = sorted(order_hash.items(), key = lambda x : [len(x[0]), -x[1]])
    for i in list_hash:
        case, val = i
        # 첫 값은 가장 큰 값이므로 삽입하고 건너뛴다.
        if not answer:
            answer.append(case)
            max_val = val
            continue
        # 코스의 첫번 째 값은 그 코스의 가장 큰 값이므로 그 값이 1보다 크면 삽입
        if len(case) != len(answer[-1]) and val>1:
            answer.append(case)
            max_val = val
        else:
            # 코스의 가장 큰 값과 같으면 삽입
            if len(case) == len(answer[-1]) and max_val == val:
                answer.append(case)
    answer.sort()
    return answer