class Solution:
    def jump(self, nums: list[int]) -> int:
        counting = [0] * len(nums)
        for i in range(len(nums)):
            for j in range(1,nums[i]+1):
                if i + j >= len(nums):
                    continue
                if counting[i+j] == 0 :
                    counting[i+j] = counting[i]+1
                    
        return counting[len(nums)-1]