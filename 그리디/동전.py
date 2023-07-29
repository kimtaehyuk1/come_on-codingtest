# 백준 11047 

N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]
ans = 0

# for문 들어갈때 거꾸로 큰거부터 들어가게 하려고
coins.reverse()
for coin in coins:
    ans += K//coin
    K %= coin

print(ans)