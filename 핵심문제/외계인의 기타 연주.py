# 백준 2841 문제 외계인의 기타 연주

# 줄은 나눠서 독립적으로 생각
# 만약 8 - 10 - 12 - 10 - 5 면 손가락 움직임이 7이다!! 일단 이거 이해
# 스택을 이용해서 구현

import sys

input = sys.stdin.readline

N, P = map(int, input().split())
# 줄이 1~6까지 필요하니까 인덱스6까지 받아주기위해 7개의 비어져 있는 스택만들기
stk = [[] for _ in range(7)]
ans = 0

for _ in range(N):
    line, p = map(int, input().split())
    while stk[line] and stk[line][-1] > p: # 각 라인에 맞는 스택이 있고, 스택 최상단이 들어온 p보다 크면 계속 빼줘야 한다.
        stk[line].pop()
        ans += 1
    
    if stk[line] and stk[line][-1] == p:
        continue  # 스택 상단 값이랑, 들어온p랑 같으면 아무 행위안하니까

    # 위 둘다 아닌경우는 스택에 쌓아주면 된다.
    stk[line].append(p)
    ans += 1

print(ans)