def solution(survey, choices):
    answer = ''
    score = [0,3,2,1,0,-1,-2,-3]
    survey_hash = {"RT" : 0, "CF" : 0, "JM" : 0, "AN" : 0}
    # 1~3번은 앞의 문자 5~7번은 뒤의 문자에 점수를 부과한다.
    for i, s in enumerate(survey):
        if  survey_hash.get(s) == None:
            survey_hash[s[::-1]] += (-score[choices[i]])
        else:
            survey_hash[s] += (score[choices[i]])
    for k, v in survey_hash.items():
        if v >= 0:
            answer += k[0]
        else:
            answer += k[1]
    return answer