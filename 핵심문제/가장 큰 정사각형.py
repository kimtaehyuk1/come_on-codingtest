# 백준 1915 큰 정사각형
# 시그마 i ** 2만큼 즉 3억개만큼 정사각형이 나온다( 1x1 = 1000*1000 개 2x2 = 999 * 999개....) 개다가 1로 다 채워졌는지 검사하면
# 완전탐색으로는 불가
# 아이디어 : DP(i,j) = i,j칸을 우하단으로 하는 정사각형의 최대크기
# i가 위아래고, j는 왼쪽오른쪽 즉 !!! DP(i,j) = min(DP(i,j-1), DP(i-1,j), DP(i-1,j-1)) + 1 이다 조건(if arr[i][j] == 1(값이 있을때)) 이런식으로 채우고 젤 큰값의 제곱이 답이다.

n, m = map(int, input().split())
# 문자열로
arr = [input() for _ in range(n)]
dp = [[0] * m for _ in range(n)]

# 우선 점화식 쓰기위해 맨 행첫줄과 맨 열 왼쪽 채우기
# 맨위 행 채우기
for j in range(m):
    if arr[0][j] == '1':
        dp[0][j] = 1

# 맨 왼쪽 열 채우기 근데 겹치는 부분은 빼줘야 하니까
for i in range(1,n):
    if arr[i][0] == '1':
        dp[i][0] =1

# 이제 점화식으로 나머지 채우기
for k in range(1,n):
    for z in range(1,m):
        if arr[k][z] == '1': #1이라는 값이 있을때만 주의: if arr[k][j] 이렇게 하면 안됨
            dp[k][z] = min(dp[k][z-1], dp[k-1][z], dp[k-1][z-1]) + 1

# dp테이블 존재 값중 젤 큰값의 제곱이 답
ans = 0
for i in range(n):
    for j in range(m):
        ans = max(ans, dp[i][j])

print(ans * ans)


    