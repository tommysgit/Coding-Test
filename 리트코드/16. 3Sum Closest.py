import bisect
class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        # num의 배열 숫자중 3개의 합이 target과 근접한 값을 return
        # 
        #nums.sort()
        closest_num = 1e9
        def binary_search(target, data):
            start = 0
            end = len(data)-1
            mid = (start + end) // 2
            gap = abs(target-data[mid])
            result = mid
            # target과 가장 가까운 수 이진탐색으로 찾기
            while start <= end:
                mid = (start + end) // 2
                # 타겟과 mid의 값의 차이의 절대값
                new_gap = abs(target-data[mid])
                if new_gap < gap:
                    gap = new_gap
                    result = mid
                if data[mid] < target:
                    start = mid + 1
                else:
                    end = mid - 1
            return data[result]
        def two_pointer():
            start = 0
            end = len(nums)-1
            combi_sum = nums[start] + nums[end] + nums[(start+end)//2]
            while end - start > 1:
                binary_target = (target-nums[start]-nums[end])
                binary_val = binary_search(binary_target, nums[start+1:end])
                tmp_sum = (nums[start] + binary_val + nums[end])
                # 기존 합계보다 더 가깝다면 combi_sum 갱신
                if abs(target - tmp_sum) < abs(combi_sum - target):
                    combi_sum = tmp_sum
                if tmp_sum < target:
                    start += 1
                else:
                    end -= 1
            return combi_sum
                
        nums.sort()
        return two_pointer()