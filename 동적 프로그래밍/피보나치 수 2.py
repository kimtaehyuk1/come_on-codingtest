# 백준 2748 피보나치 수 2

# Top-down방식으로 풀기 -> 재귀함수 이용하여서 & 메모이제이션 적용

# cache = [-1] * 91
# cache[0] = 0
# cache[1] = 1


# # 밑에께 왜 메모리상에 기억되는게 이득인지 잘 기억해보기
# def f(n):
#     if cache[n] == -1:
#         cache[n] = f(n-1) + f(n-2)

#     return cache[n]

# print(f(int(input())))


# ----------------------------------------------------------------------------
# 반복문으로 구하기

N = int(input())
cache = [-1] * 91
cache[0] = 0
cache[1] = 1

for i in range(2, N+1):
    cache[i] = cache[i -1] + cache[i - 2]


print(cache[N])

# 위의for 로 하려면 순차적으로 앞에서부터 값을 알아야 뒤에거 아닌데 top-down은 내가 원하는 부분만 쏙 빼서(함수정의만 되있으면) 구현할 수 있다.