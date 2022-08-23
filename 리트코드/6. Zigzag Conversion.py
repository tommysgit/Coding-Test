class Solution:
    def convert(self, s: str, numRows: int) -> str:
        two_array = [[] for i in range(numRows)]
        is_up = 0
        is_down = 1
        idx = 0
        for i in range(len(s)):
            two_array[idx].append(s[i])
            if numRows == 1:
                continue
            if is_down:
                # 하단 끝에 도달하면 인덱스 다시 감소
                if idx == (numRows-1):
                    idx -= 1
                    is_up = 1
                    is_down = 0
                else:
                    idx += 1
            else:
                # 상단 끝에 도달하면 인덱스 증가
                if idx == 0:
                    idx += 1
                    is_up = 0
                    is_down = 1
                else:
                    idx -= 1
        result = ''
        for array in two_array:
            for c in array:
                result += c
        return result