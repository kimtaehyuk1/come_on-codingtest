def solution(targets):
    answer = 0
    # [s,e]형태에서 e를 기준으로 오름차순 정렬
    targets.sort(key = lambda x : x[1])
    # 초기세팅
    e = 0
    # 정렬된거에서 하나씩 비교하면서 
    for target in targets:
        if e <= target[0]:
            answer += 1
            e = target[1]
    return answer



targets = [[4,5],[4,8],[10,14],[11,13],[5,12],[3,7],[1,4]]
print(solution(targets))