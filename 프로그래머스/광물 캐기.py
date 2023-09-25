from collections import deque

def solution(picks, minerals):
    answer = 0

    minerals_deque = deque() #popleft 하기위해

    for i in minerals:
        minerals_deque.append(i)


    #  picks도 순서가 고정되있고, minerals도 차례대로 캘 수 있으니 이점 이용
    # 다이아처리
    dia = picks[0]*5
    for _ in range(dia): #이만큼 돌면서 다이아는 1이니까 한번 돌때 한개씩 뺴주면됨
        if minerals_deque:
            minerals_deque.popleft()
            answer += 1
        else:
            break

    # 철 처리
    iro = picks[1]*5 #일단 개수로는 이만큼 처리할건데 피로도를 곁들여야겠죠
    for _ in range(iro):
        if minerals_deque:
            tmp1 = minerals_deque.popleft()
            if tmp1 == 'diamond':
                answer += 5
            else:
                answer += 1
        else:
            break

    # 돌 처리
    sto = picks[2]*5
    for _ in range(sto):
        if minerals_deque:
            tmp2 = minerals_deque.popleft()
            if tmp2 == 'diamond':
                answer += 25
            if tmp2 == 'iron':
                answer += 5
            if tmp2 == 'stone':
                answer += 1
        else:
            break

    return answer

picks = [1, 3, 2]
minerals = ["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"]
print(solution(picks,minerals))


