from collections import Counter
def solution(n, lost, reserve):
    lost, reserve = list(set(lost) - set(reserve)), list(set(reserve)-set(lost))
    answer = n - len(lost)
    reserve_hash = Counter(reserve)
    for i, v in enumerate(lost):
        if v-1 in reserve_hash.keys():
            answer += 1
            del reserve_hash[v-1]
        elif v+1 in reserve_hash.keys():
            answer += 1
            del reserve_hash[v+1]
    
            
    return answer