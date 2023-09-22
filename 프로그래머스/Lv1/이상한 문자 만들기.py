def solution(s):
    answer = []

    s_list = [i for i in s.split()]

    for i in s_list:
        # 변환후 각 단어를 다시 만들 문자열
        modi_word = ''
        for j,k in enumerate(i):
            if j % 2 == 0:
                modi_word += k.upper()
            else:
                modi_word += k.lower()
        
        answer.append(modi_word)

    # 여기서 마지막으로 []안에 있는 문자열들 가지고 공백으로 구분지어서 합치기
    answer = ' '.join(answer)

    return answer


s = "try hello world"
print(solution(s))