
# def solution(sequence, k):
#     answer = []
    
#     n = len(sequence)
#     # for를 돌면서 한번 sequence길이만큼 일일이 연속된거 다 더해보자
#     for i in range(1,n+1): # 1씩 연속부터 n개씩 연속인거 돌리려고 쓴 for문
#         for j in range(n-i+1): # 이 수식 중요
#             total = sum(sequence[j:j+i])
#             if total == k:
#                 # 그거에 맞는 인덱스만 뽑아내면 끝
#                 answer.append(j)
#                 answer.append(j+i-1)
#                 return answer
            
# ----------------------------------------------------------------시간초과남.

# 예시 [1,2,3,4,5]
# 레전드 풀이 : 이런게 있구나~ 정도만
def solution(sequence, k):
    answer = []
    sum = 0
    r = -1
    l = 0
    while True:
        if sum < k:
            r += 1
            if r >= len(sequence):
                break
            sum += sequence[r]
        else: # 이경우는 sum이 k보다 크거나 '같은' 경우도 포함이다. # 같아져도 l로 빠지면 또 sum < k 이걸타서 또 r 증가하면서 가는거
            sum -= sequence[l]
            if l >= len(sequence):
                break
            l += 1
        if sum == k:
            answer.append([l,r])

    answer = sorted(answer, lambda i: (i[1]-i[0], i[0] )) #이것은 처음비교는 들어오는 값에서 1인덱스 - 0인덱스가 작은순으로, 
                    # 그다음 같으면 앞에있는거 순으로 인덱스 값 순으로 
    return answer[0]



