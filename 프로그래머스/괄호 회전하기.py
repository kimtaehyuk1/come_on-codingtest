from collections import deque
def solution(s):
    answer = 0

    # 회전하든 안하든 괄호 넣을떄 올바른 괄호인지 알려주는 함수 짜기
    def colletion(n):
        stk = []
        for ch in n:
            if ch in '([{':
                stk.append(ch)
            else:
                if not stk: # 처음부터 닫는 괄호 있는 경우
                    return False 
                if ch == ')' and stk[-1] == '(':
                    stk.pop()
                elif ch == ']' and stk[-1] == '[':
                    stk.pop()
                elif ch == '}' and stk[-1] == '{':
                    stk.pop()
                else: # [} 이런경우
                    return False
        # 다 맞는경우 1처리
        return len(stk) == 0  # 이게 맞으면 True 

    # 큐에 s 넣기 -> 왜냐? 앞에서 부터 뺴야하니까
    dq_s = deque(s)

    # 돌면서 회전하기
    for j in range(len(s)):
        if colletion(dq_s):
            answer += 1
        tmp = dq_s.popleft()
        dq_s.append(tmp)

    return answer


s = '}]()[{'
print(solution(s))