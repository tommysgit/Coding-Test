class Solution:
    def longestPalindrome(self, s: str) -> str:
        answer = ''
        def two_pointer(i):
            left, right = i, i
            # 중심점을 기준으로 좌우로 한칸씩 넓혀간다.
            while 0 <= left:
                if s[i] == s[left]:
                    left -= 1
                else:
                    break
            while right < len(s):
                if s[i] == s[right]:
                    right += 1
                else:
                    break
            while 0 <= left and right < len(s):
                if s[left] == s[right]:
                    left -= 1
                    right += 1
                else:
                    break
            return s[left+1 : right]
        for i in range(len(s)):
            answer = max(answer, two_pointer(i), key = len)
        return answer