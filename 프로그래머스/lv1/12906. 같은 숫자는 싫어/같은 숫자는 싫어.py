def solution(arr):
    answer = []
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    prev = arr[0]
    answer.append(prev)
    for i in range(1, len(arr)):
        if arr[i] !=prev:
            answer.append(arr[i])
        prev = arr[i]
    return answer