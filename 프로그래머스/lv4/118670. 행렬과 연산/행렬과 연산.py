from collections import deque
def solution(rc, operations):
    answer = []
    r_len, c_len = len(rc), len(rc[0])
    
    rows = deque(deque(rc[i][1:-1]) for i in range(r_len))
    cols = [deque(rc[r][0] for r in range(r_len)),
            deque(rc[r][c_len-1] for r in range(r_len))]

    for order in operations:
        # shift row
        if order[0] == 'S':
            rows.appendleft(rows.pop())
            cols[0].appendleft(cols[0].pop())
            cols[1].appendleft(cols[1].pop())
        # rotate
        # rows[0][:-1] -> cols[1][0] , cols[1][:-1] -> rows[c_len-1][:-1]
        # rows[c_len-1][0] -> cols[0][:-1], cols[0][0] -> rows[0][0]
        else: 
            rows[r_len-1].append(cols[1].pop())
            cols[0].append(rows[r_len-1].popleft())
            rows[0].appendleft(cols[0].popleft())
            cols[1].appendleft(rows[0].pop())
            

    for i in range(r_len):
        answer.append([cols[0][i]]+ list(rows[i]) + [cols[1][i]] )
    return answer