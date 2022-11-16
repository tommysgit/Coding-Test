def solution(name):
    global min_dis
    min_dis = 1e9
    def back_track(n, is_visit, cnt):
        global min_dis
        if sum(is_visit) == len(is_visit):
            min_dis = min(min_dis, cnt)
            return
        for i in range(len(is_visit)):
            if is_visit[i] == 1:
                continue
                
            # i가 n의 왼쪽으로 몇칸인지 오른쪽으로 몇칸인지 구분한다.
            if i > n:
                r = i - n
                l = (len(is_visit) - i) + n
            else:
                l = n - i
                r = (len(is_visit) - n) + i
            # 왼쪽, 오른쪽
            is_visit[i] = 1
            if l < r:
                back_track(i, is_visit, cnt+l)
            elif l > r:
                back_track(i, is_visit, cnt+r)
            else:
                back_track(i, is_visit, cnt+l)
                back_track(i, is_visit, cnt+r)
            is_visit[i] = 0
            
            
            
    alphabet = [ min(ord(c) - ord('A'), ord('Z') - ord(c)+1) for c in name]
    answer, cursor = 0, 0
    is_visit = [0]*len(name)
    is_visit[0] = 1
    for i in range(len(name)):
        if name[i] == 'A':
            is_visit[i] = 1
    back_track(0, is_visit, 0)
    answer = min_dis + sum(alphabet)

                
        
    return answer