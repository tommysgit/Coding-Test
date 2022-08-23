class Solution:
    def maxArea(self, height: list[int]) -> int:
        answer = 0

        def two_pointer():
            max_val = 0
            left = 0
            right = len(height) - 1
            while left < right:
                left_y = height[left]
                right_y = height[right]
                x_len = right - left
                y_len = min(left_y, right_y)
                val = x_len * y_len
                if val > max_val:
                    max_val = val
                if left_y == right_y:
                    left += 1
                    right -= 1
                elif left_y > right_y:
                    right -= 1
                else:
                    left += 1
            return max_val

        answer = two_pointer()
        return answer
            