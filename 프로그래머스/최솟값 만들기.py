def solution(A,B):
    answer = 0
    # A에서 가장 작은 수와 B에서 가장 큰수 뽑아서 곱해서 더하기
    A.sort()
    B.sort(reverse = True)
    
    for k,j in zip(A,B):
        answer += (k*j)


    return answer



A = [1, 4, 2]
B = [5, 4, 4]
print(solution(A,B))