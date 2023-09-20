import math
def solution(n):
    answer = 0
    
    # 소수찾는 알고리즘
    def prime(x):
        if x <= 1:
            return False
        if x == 2:
            return True
        
        for i in range(2, int(math.sqrt(x))+1):
            if x % i == 0:
                return False
        return True 


    for i in range(1,n+1): #n까지의 소수를 알아보는 경우의 수
        if prime(i):
            answer += 1
    
    
    return answer

print(solution(5))