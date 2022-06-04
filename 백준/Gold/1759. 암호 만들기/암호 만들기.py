# 1759
L, C = map(int, input().split())
# L = 최소 한 개의 모읍 + 최소 두 개의 자음
# C개의 문자열에서 L개의 오름차순 조합 문자열 추출
cyper = list(map(str, input().split()))
cyper.sort()
stack = []
def combi(start):


    if len(stack) == L:
        str_cyper = "".join(stack)
        count = 0
        for i in str_cyper:
            if i in "aeiou":
                count+=1
        if count>0 and len(stack) - count>1:
            print(str_cyper)
        return
    for i in range(start, len(cyper)):

        stack.append(cyper[i])
        combi(i+1)
        stack.pop()
combi(0)
