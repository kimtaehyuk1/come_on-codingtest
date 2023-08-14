# m = {}
# m["taehyuk"] = 100
# m["taejun"] = 200
# for k in m:
#     print(k,m[k])

# A = [2,7,3,4,1]

# I = list(range(5))

# I = sorted(I, key= lambda i: A[i])

# print(I)


# N, K = map(int, input().split())
# coins = [int(input()) for _ in range(N)]
# coins.reverse()

# print(coins)


# for i in range(7,7):
#     print(i)

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