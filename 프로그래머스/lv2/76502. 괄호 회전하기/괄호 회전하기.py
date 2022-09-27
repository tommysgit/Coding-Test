from collections import deque
def solution(s):
    answer = 0
    bracket_hash = { ')' : '(', ']' : '[' , '}' : '{'}
    q = deque(s)
    
    def check(brackets):
        stack = []
        for bracket in brackets:
            if bracket in bracket_hash:
                if stack:
                    if bracket_hash[bracket] != stack.pop():
                        return False
                else:
                    return False
            else:
                 stack.append(bracket)   
        if stack:
            return False
        return True

    for i in range(len(s)):
        q.append(q.popleft())
        if check(''.join(q)):
            answer += 1
    
    return answer