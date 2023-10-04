def solution(n):
    
    # dp[n]은 n칸까지 뛸 수 있는 방법의 수
    # 그 방법은 

    if n <= 2:
        return n

    dp = [0] * (n+1)
    dp[1] = 1
    dp[2] = 2
    for i in range(3,n+1):
        dp[i] = (dp[i-1]+dp[i-2]) % 1234567


    return dp[n]

n = 3
print(solution(n))