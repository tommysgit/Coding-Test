class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        num_hash = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        answer = []
        def back_track(s, start):
            if len(s) == len(digits):
                answer.append(s)
                return 
            num = digits[start]
            c = num_hash[num]
            for i in range(len(c)):
                back_track(s + c[i], start + 1)
        if len(digits) > 0:
            back_track("", 0)
        return answer
                