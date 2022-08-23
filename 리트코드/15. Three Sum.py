class Solution:
    
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        answer = []
        nums.sort()
        # nums[i]는 기준점
        for i in range(len(nums)-2):
            # 중복 방지 -4 -1 -1 0 1 2 
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:                
                three_sum = nums[left] + nums[i] + nums[right]
                if three_sum < 0:
                    left += 1
                elif three_sum > 0 :
                    right -= 1
                else:
                    # 합이 0인경우
                    answer.append([nums[left],nums[i],nums[right]])
                    # 같은이 나오면 넘긴다.
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
        return answer
