from copy import deepcopy
from itertools import combinations_with_replacement
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        answer = []
        def back_track(stack, left, right):
            if len(stack)== n*2:
                answer.append("".join(stack))
                return
            if left < n:
                stack.append('(')
                back_track(stack, left + 1, right)
                stack.pop()
            if right < left:
                stack.append(')')
                back_track(stack, left, right + 1)
                stack.pop()
        back_track([], 0, 0)
        return answer
                
                