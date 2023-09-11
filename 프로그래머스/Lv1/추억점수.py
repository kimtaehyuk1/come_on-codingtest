# https://school.programmers.co.kr/learn/courses/30/lessons/176963

def solution(name, yearning, photo):
    answer = []
    score_dic = {}
    for name1, score in zip(name, yearning):
        score_dic[name1] = score
        
    for elem in photo:
        temp = 0
        for el in elem:
            if el in score_dic:
                temp += score_dic[el]
        answer.append(temp)    
    
    return answer