# 문제 url : https://www.acmicpc.net/problem/9012
# 올바른 괄호 쌍 문제
# 접근: 먼저 들어온 ( 여는 괄호는 나중에 들어온 맨마지막 ) 괄호와 매칭 -> 스택이다.

for _ in range(int(input())):
    stk = []
    isVPS = True
    for ch in input(): 
        if ch == '(':
            stk.append(ch)
        else:
            if stk:   # (()) ) 마지막볼땐 리스트 비워져 있을텐데 이러면 없는데  pop하면 안되니까 오류남.
                stk.pop()
            else:
                isVPS = False
                break
    
    if stk:
        isVPS = False

    print('YES' if isVPS else 'No')


# 범 풀이
def sol(sentence):
    answer = []
    for elem in sentence:
        answer.append(elem)
        if len(answer) >= 2:
                if answer[-1] == ")" and answer[-2] == "(":
                        answer.pop()
                        answer.pop()

    if len(answer) == 0:
        return 'YES'
    else:
        return 'NO'