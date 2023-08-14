# 백준 10799번 문제

# 일단 무조건 스택문제고 이해해야 되는데,
# 1. (는 스택에 쌓고 ) 이게 왔을때 전에 (였으면 레이저니까 (한개 pop하고 스택에있는( 개수 세기 
# 2. )인데 전께 )였으면 스택에 있는 (이거 하나 pop하고 +1 해주기 (쇠막대기 1개 레이저 두번이면 쇠막대기 3개니까 뒤에 +1처리)

input = list(input())
stk = []
cnt = 0


for ch in range(len(input)): 
    if input[ch] == '(':
        stk.append('(')
    else:
        if input[ch-1] == '(':    #전껏이 뭐였냐 처리
            stk.pop()
            cnt += len(stk)
        else:
            stk.pop()
            cnt += 1

print(cnt)