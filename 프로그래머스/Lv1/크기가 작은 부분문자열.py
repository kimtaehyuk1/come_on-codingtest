def solution(t, p):
    answer = 0

    t_len = len(t)
    p_len = len(p)
    p_int = int(p)

    for i in range((t_len-p_len)+1):
        sub_t = int(t[i:(i+p_len)])

        if sub_t <= p_int:
            answer += 1

    return answer


t = "10203"
p = "15"

print(solution(t,p))