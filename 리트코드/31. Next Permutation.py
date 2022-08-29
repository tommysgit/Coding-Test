
class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 가장 큰 수의 인덱스
        N = len(nums) - 1
        i = N
        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1
        top = i
        if top == 0:
            nums.sort()
            return
        # 가장 큰 수 인덱스의 앞의 값들 중 꼭대기 보다 작은 값 찾기
        #print(nums)
        for i in reversed(range(top)):
            if nums[i] < nums[top]:
                swap_a = i
                break
        # 뒤에서부터 swap_a보다  큰 swap_b를 구한다.
        for i in reversed(range(len(nums))):
            if nums[swap_a] < nums[i]:
                swap_b = i
                break
        
        
        nums[swap_a] , nums[swap_b] = nums[swap_b], nums[swap_a]
        tmp = nums[swap_a+1:]
        tmp.sort()
        #print(swap_a, swap_b, nums, nums[swap_a+1:], tmp)
        nums[swap_a+1:] = tmp