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
    for i in range(len(relation[0])):
        # 유일성 : i+1개의 속성이 고유해야함
        # 최소성 : 유일성이 최소값이어야함 
        # i번째를 지날때 마다 
        primary = []
        for j in list(itertools.combinations(target, i+1)):
            j = list(j)
            is_continue = 0
            # fix의 원소가 j에 있으면 continue
            for e in fix:
                #print(set(j) , set(e) , len(j) , len(e))
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