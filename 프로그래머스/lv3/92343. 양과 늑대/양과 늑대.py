def solution(info, edges):
    answer = 0
    stack = []
    stack.append(0)
    is_visit = [0] * len(info)
    is_visit[0] = 1
    max_num = [0]
    # 이진 트리 규칙
    # 늑대 < 양 의 수를 만족하는 조건 하에 양이 나올때 까지 탐색
    # 탐색 시 다음 탐색 경로가 없으면 pop
    # 양 얻을 때 마다 그 상태에서 non visited 경로 탐색
    
    def back_track(sheep, wolf):
        #print(sheep, wolf)
        #global max_num
        if sheep == wolf:
            return
        max_num[0] = max(max_num[0], sheep)
        for i in edges:
            parent, child = i
            if is_visit[parent] == 0:
                continue
            is_wolf = info[child]
            add_wolf = 1 if is_wolf else 0
            add_sheep = 1 if not is_wolf else 0
            if is_visit[child] == 0 :
                is_visit[child] = 1
                back_track(sheep + add_sheep, wolf + add_wolf)
                is_visit[child] = 0

    back_track(1,0)
    return max_num[0]