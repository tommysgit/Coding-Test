import sys
sys.setrecursionlimit(100000)
def solution(nodeinfo):
    answer = [[] for i in range(2)]
    for i in range(len(nodeinfo)):
        nodeinfo[i].append(i+1)
    nodeinfo.sort(key = lambda x : [-x[1], x[0]])
    is_visit1 = [0]*(len(nodeinfo)+1)
    is_visit2 = [0]*(len(nodeinfo)+1)
    def pre_order(start, left, right):
        # 왼쪽과 오른쪽을 찾는다.
        
        # i번째 방문 노드정보를 꺼내고 방문처리
        x, y, num = nodeinfo[start]
        is_visit1[start] = 1
        answer[0].append(num)
        
        for i in range(start, len(nodeinfo)):
            next_x, next_y, next_num = nodeinfo[i]
            # 이미 방문한 노드 혹은 같은 계층의 노드는 건너뛴다.
            if is_visit1[i] == 1 or next_y == y:
                continue
            # 왼쪽 노드방문하는 경우
            if next_x < x and left < x:
                pre_order(i, left ,x)
            # 오른쪽 노드 거치면 탈출
            elif next_x > x and next_x < right:
                pre_order(i, x, right)
                break
    def post_order(start, left, right):
        x, y, num = nodeinfo[start]
        is_visit2[start] = 1
        
        for i in range(start, len(nodeinfo)):
            next_x, next_y, next_num = nodeinfo[i]
            # 이미 방문한 노드 혹은 같은 계층의 노드는 건너뛴다.
            if is_visit2[i] == 1 or next_y == y:
                continue
            # 왼쪽 노드방문하는 경우
            if next_x < x and left < x:
                post_order(i, left ,x)
            # 오른쪽 노드 거치면 탈출
            elif next_x > x and next_x < right:
                post_order(i, x, right)
                break
        answer[1].append(num)
    pre_order(0, -1, 1e9)
    
    post_order(0, -1, 1e9)
    # print(answer)
    return answer