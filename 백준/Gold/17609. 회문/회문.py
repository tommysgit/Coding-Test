# 14503
import sys

T = int(input())
def division_string(s):
    start = 0
    end = len(s) -1
    #count = 0
    while start < end:
        #print(start, end, s[start], s[end])
        # 반대편 자리의 문자와 같으면
        if s[start] == s[end]:
            start += 1
            end -= 1
            continue
        # 다르면
        else:
            # start 증가시킨 값과 end값이 같고
            # 해당 시점을 시작으로 끝날때 까지 맞다면 1로 break
            if s[start+1] == s[end] :
                # start를 하나 더 증가시킬 때 그 다음 번 순에도 같은지 확인 후 증가
                tmp_start , tmp_end = start+1, end
                # if s[start+2] == s[end-1]:
                #     start += 1
                # start += 1
                res = 1
                while tmp_start < tmp_end :
                    if s[tmp_start] == s[tmp_end]:
                        tmp_start +=1
                        tmp_end -= 1
                        continue
                    else:
                        res = 0
                        break
                if res == 1:
                    return 1
            if s[start] == s[end-1] :
                tmp_start , tmp_end = start, end - 1
                res = 1
                while tmp_start < tmp_end :
                    if s[tmp_start] == s[tmp_end]:
                        tmp_start +=1
                        tmp_end -= 1
                        continue
                    else:
                        res = 0
                        break
                if res == 1:
                    return 1
            return 2
        
    return 0
for i in range(T):
    string = sys.stdin.readline().strip()
    cnt = division_string(string)
    print(cnt)
