from collections import *
from itertools import *
from bisect import *
def solution(info, query):
    answer = []
    hash_info = {}
    # 아무 조건 없을 때를 대비하여 추가
    hash_info["default"] = []
    
    for i in info:
        # 문자열을 리스트로 바꿔 파싱하기 편하게 한다.
        tmp_str = i.split()
        score = tmp_str.pop()
        for j in range(1, 5):
            for k in combinations(tmp_str, j):
                combi_str = ''.join(k)
                if not hash_info.get(combi_str):
                    hash_info[combi_str] = []
                hash_info[combi_str].append(int(score))

        hash_info["default"].append(int(score))
    for i in hash_info:
        hash_info[i].sort()
    # query 파싱
    for i in query:
        parsed_query = i.split()
        score = parsed_query.pop()
        score = int(score)
        parsed_query = [q for q in parsed_query if '-' not in q and 'and' not in q]
        if not parsed_query:
            search_condition = 'default'
        else:
            search_condition = ''.join(parsed_query)
        # print("s")
        # print(search_condition, hash_info[search_condition])
        if hash_info.get(search_condition):
            nums = hash_info[search_condition]
            index = len(nums)
            index = bisect_left(nums, score)
            answer.append(len(nums) - index)
            #print(hash_info[search_condition].index(score))
        else:
            answer.append(0)
        #print('a b c d e'.split(), 'a b c d e'.split(' '), 'a b c d e'.split(''))
    return answer