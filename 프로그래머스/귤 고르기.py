
# 나이스 풀이~~~

def solution(k, tangerine):
    answer = 0
    # 딕셔너리로 어떤 숫자가 몇개있는지 짜주기
    cnt_num = {}
    
    for i in tangerine:
        if i in cnt_num:
            cnt_num[i] += 1
        else:
            cnt_num[i] = 1

    # 이후에 딕셔너리를 개수가 많은(value값이 큰 순으로)순으로 정렬
    sorted_cnt = sorted(cnt_num.items(), key = lambda x: x[1], reverse= True) # 출력 형태 : [(3, 2), (2, 2), (5, 2), (1, 1), (4, 1)]
    # 정렬된 items()에서 값만 뽑아서 리스트에 담기
    sorted_value = [val for num,val in sorted_cnt]  # [2, 2, 2, 1, 1]
    
    # for돌면서 종류 +1 하면서 k 가지고 놀기
    for j in sorted_value:
        if k <= 0:
            break
        k -= j
        answer += 1 

    return answer

k = 4
tangerine = [1, 3, 2, 5, 4, 5, 2, 3]

print(solution(k,tangerine))