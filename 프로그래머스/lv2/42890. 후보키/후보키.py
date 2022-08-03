import itertools
import copy
def solution(relation):
    answer = 0
    col_relation = list(zip(*relation))
    target = [i for i in range(len(relation[0]))]
    fix = []
    def str_sum(list1, list2):
        tmp_list = []
        for i in range(len(list1)):
            tmp_list.append(list1[i] + list2[i])
        return copy.deepcopy(tmp_list)
    # 컬럼의 개수만큼 반복문
    for i in range(len(relation[0])):
        # 유일성 : i+1개의 속성이 고유해야함
        # 최소성 : 유일성이 최소값이어야함 
        primary = []
        # 후보키가 가능한 경우의 수 조합을 만든다.
        for j in list(itertools.combinations(target, i+1)):
            j = list(j)
            is_continue = 0
            # fix안의 값은 최소성을 만족하는 후보키 이므로 j조합은 후보키가 될 수 없다.
            for e in fix:
                if len(set(j) - set(e)) == len(j) - len(e):
                    is_continue = 1
                    break
            if is_continue:
                continue
                
            # j 인덱스들의 문자열을 합친다.
            tmp_str = col_relation[j[0]]
            for k in range(1, len(j)):
                    
                tmp_str = str_sum(tmp_str, col_relation[j[k]])
            #print(tmp_str)
            if len(tmp_str) == len(set(tmp_str)):
                answer += 1
                fix.append(j)
                    
        # for remove_val in primary:
        #     target.remove(remove_val)
    return answer