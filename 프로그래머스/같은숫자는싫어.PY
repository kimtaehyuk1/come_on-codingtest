# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/12906?language=python3


def solution(arr):
    answer = []
    
    for elem in arr:
        if len(answer) == 0:
            answer.append(elem)
        else:
            if answer[len(answer) - 1] == elem:
                continue
            else:
                answer.append(elem)
            
    return answer