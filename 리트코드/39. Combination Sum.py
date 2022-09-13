from copy import deepcopy
class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        # candidates에 있는 값으로 target을 만들 수 있는 경우를 반환
        # for i in range(1, len(candidates)):
        #     for combi in combinations(candidates, i):
        answer = []
        def back_track(stack, idx):
            if sum(stack) > target:
                return
            elif sum(stack) == target:
                answer.append(deepcopy(stack))
                return
            for i in range(idx, len(candidates)):
                stack.append(candidates[i])
                back_track(stack, i)
                stack.pop()
        candidates.sort()
        back_track([], 0)
        return answer