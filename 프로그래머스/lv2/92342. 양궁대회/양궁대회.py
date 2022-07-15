from collections import deque
from copy import deepcopy
import sys
import itertools
sys.setrecursionlimit(10000000)
def solution(n, info):
    cases = []
    stack = []
    answer = []
    answer.append(-1)
    max_score = [0]
    def cal_score(apeach, ryan):
        a_score = 0
        r_score =0
        for i in range(11):
            if ryan[i] > apeach[i]:
                r_score += (10-i)
            elif apeach[i] != 0 and apeach[i] >= ryan[i]:
                a_score += (10-i)
        return r_score - a_score
    def cal_tai(exit_target, new_target):
        for i in reversed(range(11)):
            if exit_target[i] < new_target[i]:
                return 1
            if exit_target[i] != 0 and exit_target[i] >= new_target[i]:
                return 0
    def use_remain_arrow(target_list, n):
        target_list[10] += n
    def dfs(n, idx):            
        # 과녁을 다돌았으면
        if len(stack) == 11:
            # 남는 화살은 가장 낮은 점수를 쏜다.
            if n>0:
                use_remain_arrow(stack, n)
            # 점수 계산
            diff = cal_score(info, stack)
            # 점수차가 기존과 같으면 기존 점수와 낮은 값부터 비교
            if max_score[0] != 0 and diff == max_score[0]:
                result = cal_tai(cases[0], stack)
                if result == 1:
                    max_score[0] = diff
                    if cases:
                        cases.pop()
                    cases.append(deepcopy(stack))
            # 점수차가 기존 최고 점수보다 크면 갱신    
            elif diff > max_score[0]:
                if cases:
                    cases.pop()
                cases.append(deepcopy(stack))
                max_score[0] = diff
            return
        for i in range(n+1):
            if i <= n:
                stack.append(i)
                dfs(n-i, idx+1)
                stack.pop()
    dfs(n, 0)
    if not cases:
        return answer
    else:
        return cases[0]
