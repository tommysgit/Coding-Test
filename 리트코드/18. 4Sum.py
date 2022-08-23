from itertools import combinations
class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        answer = []

        nums.sort()
        for i, num in enumerate(nums):
            # 중복 방지
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            # i번째 num을 고정하고 l1, l2 , r 을 이용하여 돌려준다.
            l1= i + 1
            t = len(nums)-1
            while l1 < t:
                l2 , r= l1 + 1, len(nums) - 1
                while l2 < r:
                    #print(num, nums[l1], nums[l2], nums[r])
                    four_sum = num + nums[l1] + nums[l2] + nums[r]
                    if four_sum > target:
                        r -= 1
                    elif four_sum < target:
                        l2 += 1
                    else:
                        if [num, nums[l1], nums[l2], nums[r]] not in answer:
                            answer.append([num, nums[l1], nums[l2], nums[r]])
                        l2 += 1
                        # 중복 방지
                        while l2 < r and nums[l2] == nums[l2-1]:
                            l2 += 1
                l1 += 1


        return answer
