def solution(number, k):
    answer = ''
    
    # 스택으로 구현
    stk = []
    
    for i in number:

        while stk and k > 0 and stk[-1] < i:
            stk.pop()
            k -= 1
        stk.append(i)

    # k가 남는경우가 생김. 예를들어 54321 걍 뒤에서 부터 pop하면됨
    while k > 0:
        stk.pop()
        k -= 1

    
    # 합치기
    ans = ''.join(stk)


    return ans


number = "4177252841"
k = 4
print(solution(number,k))