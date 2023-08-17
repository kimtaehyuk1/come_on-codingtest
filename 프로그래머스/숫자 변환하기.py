# 다이나믹 프로그래밍 사용 dp 사용하여 중복되는 연산을 피하기 위해 결과를 저장하는 기법 이를 위해 배열을 사용하여 중간 결과 저장

# 이 알고리즘은 공식 처러 외워서 응용하자

def solution(x, y, n):
    
    
    if x == y:
        return 0
    
    if x > y:
        return -1
    
    if x < y:
        # dp 테이블 만들기
        dp = [float('inf')] * (y+1) # 편하게 인덱스로 y까지 가기 위함
        # 아이디어: dp[i] 는 숫자 i까지 가기위한 최소 카운트이다
        # 초기값
        dp[x] = 0
        # for로 x부터 y까지 쭉가면서 체크
        for i in range(x,y+1):
            if dp[i] == float('inf'):
                continue
            if i+n <= y:
                dp[i+n] = min(dp[i+n],dp[i]+1) 
            if i*2 <= y:
                dp[i*2] = min(dp[i*2],dp[i]+1)
            if i*3 <= y:
                dp[i*3] = min(dp[i*3],dp[i]+1)
                
        if dp[y] == float('inf'):
            return -1
        
    return dp[y]

print(solution(10,40,30))