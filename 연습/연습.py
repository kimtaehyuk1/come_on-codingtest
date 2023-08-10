# m = {}
# m["taehyuk"] = 100
# m["taejun"] = 200
# for k in m:
#     print(k,m[k])

# A = [2,7,3,4,1]

# I = list(range(5))

# I = sorted(I, key= lambda i: A[i])

# print(I)


N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]
coins.reverse()

print(coins)