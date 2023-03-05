'''
문제 url : https://www.acmicpc.net/problem/2512
'''

# 입력
n = int(input()) # 지방 수
requests = list(map(int,input().split())) # 지방 당 요청예산 입력 # input().split()을 해야 리스트로 갈린다
budget = int(input()) # 정부가 줄수 있는 총예산

# 상한액이 upper_bound일때 필요 예산을 계산하는 함수
def calculate_needed_budget(upper_bound: int) -> int:
    needed_budget = 0
    for request in requests:
        needed_budget += min(request, upper_bound)
    
    return needed_budget

# 이분탐색을 수행하는 메인로직
low = 0
high = max(requests)
choice_upper_bound = -1

while low <= high:
    mid = (low + high) // 2  

    if calculate_needed_budget(mid) <= budget:
        choice_upper_bound = mid
        low = mid + 1
    else:
        high = mid - 1

# 출력, 출력은 지방이 요청한거 참고해서 최종 정부가 가진 돈을 지방에게 나눠 줬을때 지방이 받은 최대값임.
# 수정 최종 풀이
answer = min(choice_upper_bound,max(requests))
print(answer)

#answer = -1
#for request in requests:
#    tmp = min(request,choice_upper_bound)
#    answer = max(answer,tmp)
#print(answer)