import re
import copy
def solution(str1, str2):
    answer = 0
    test = re.compile('[a-zA-Z]{2}')
    str1_list = []
    str2_list = []
    # 교집합 곂치는 값만 삽입
    def intersection(list1, list2):
        tmp1 = copy.deepcopy(list1)
        tmp2 = copy.deepcopy(list2)
        result = []
        for a in tmp1:
            if a in tmp2:
                tmp2.remove(a)
                result.append(a)
        return result
    # 합집합 a와 b를 더하고 교집합을 뺀다.
    def union(list1, list2):
        result = list1 + list2
        intersection_list = intersection(list1, list2)
        for val in intersection_list:
            if val in result:
                result.remove(val)
        return result
    
    def cal(set1, set2):
        print(set1, set2)
        intersection_list = intersection(set1, set2)
        union_list = union(set1, set2)
        #print(intersection, union, set1, set2)
        if not intersection_list and not union_list:
            return 65536
        return int(len(intersection_list) / len(union_list) * 65536)
    # str1
    for i in range(len(str1)-1):
        s1 = str1[i:i+2]
        if test.fullmatch(s1):
            str1_list.append(s1.upper())
    # str2
    for i in range(len(str2)-1):
        s2 = str2[i:i+2]
        if test.fullmatch(s2):
            str2_list.append(s2.upper())
    answer = cal(str1_list, str2_list)
 
    return answer