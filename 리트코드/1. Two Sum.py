class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        my_hash = {}
        # hash에 삽입
        for i, num in enumerate(nums):
            my_hash[num] = i
        # i번째를 뺀 값이 hash에 있는지 확인
        for i, num in enumerate(nums):
            diff = target - num
            if diff in my_hash and i != my_hash[diff]:
                return [i, my_hash[diff]]
        