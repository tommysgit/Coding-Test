class Solution:
    def reverse(self, x: int) -> int:
        
        s = str(x)

        if s[0] == '-':
            x = -int(s[len(s)-1:0:-1])
        else:
            x = int(s[::-1])
        if x < -2**31 or x > 2 ** 31 - 1:
            return 0
        return x
        