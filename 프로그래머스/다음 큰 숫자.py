def solution(n):

    answer = n + 1

    # 주워진 n을 이진수로 바꾸기
    bi_n = bin(n)[2:]
    # bi_n 1의 개수 세기
    cnt_one_bin = bi_n.count('1')

    while True:
        
        # 한개씩 올린놈의 이진수 바꾸기
        bi_ans = bin(answer)[2:]
        # bi_ans의 1의 개수 세기
        cnt_one_ans = bi_ans.count('1')

        # 만약 1의 개수가 bi_n과 같으면 종료하기
        if cnt_one_bin == cnt_one_ans:
            break

        answer += 1

    return answer


n = 15
print(solution(n))