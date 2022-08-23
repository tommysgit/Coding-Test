class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 반복하지않는 가장 긴 문자열의 길이를 반환
        count = 0
        max_count = 0
        strs = ''
        # dvdf
        # vdf
        for c in s:
            overlap_idx = strs.find(c)
            # str에 문자 c가 들어있으면
            if  overlap_idx >= 0:
                # str은 c의 첫 인덱스 다음 인덱스부터 시작
                # count는 str의 길이로 갱신
                strs = strs[overlap_idx+1:]
                strs += c
                count = len(strs)
            # str에 문자 c가 없으면 str에 추가, count up
            else:
                strs += c
                count += 1
            if count > max_count:
                max_count = count
        return max_count