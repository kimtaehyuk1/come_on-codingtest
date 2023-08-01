# 백준 11051 이항 계수 2
# import sys
# sys.setrecursionlimit(10 ** 7)

# MOD = 10007

# cache = [[0] * 1001 for _ in range(1001)] #인덱스가 0부터 1000까지 들어가야 되니까 2차원 배열로 메모이제이션
# N, K = map(int,input().split())


# # 이항계수 공식 : bino(n,k) = bino(n-1,k-1) + bino(n-1,k) 이다. 이걸이용
# def bino(n,k):
#     if cache[n][k]:
#         return cache[n][k]
    
#     if k == 0 or k == n:
#         cache[n][k] = 1
#     else:
#         cache[n][k] = bino(n-1,k-1) + bino(n-1,k)
#         cache[n][k] %= MOD  # 이쪽만 MOD로 나눠주면 다른쪽은 무조건 10007안넘는거 보장되있으니까
    
#     return cache[n][k]
    
# print(bino(N,K))


# --------------------------------------------------------------------------------------------for 문으로도


MOD = 10007

cache = [[0] * 1001 for _ in range(1001)] #인덱스가 0부터 1000까지 들어가야 되니까 2차원 배열로 메모이제이션
N, K = map(int,input().split())

for i in range(1001):
    cache[i][0] = cache[i][i] = 1
    for j in range(1, i):  #j는 1부터 i-1까지니까
        cache[i][j] = cache[i-1][j-1] + cache[i-1][j]
        cache[i][j] %= MOD

print(cache[N][K])