from itertools import combinations


def solution(d, budget):
    answer = 0
    
    d.sort()

    for i in d:
        if i <= budget:
            answer +=1
            budget -= i
        else:
            break

    return answer



d = [1,3,2,5,4]
budget = 9
print(solution(d, budget))


##### 밑에도 풀이 됨.
# def solution(d, budget):
#     answer = 0

#     # 안쪽에 for문에서 break를 만나면 밖에도 멈춰주기위한 변수 설정
#     stop_outer = False

#     # 거꾸로 부터 해서 다더해서 budget 넘지않으면 그 i찍고 break하는걸로
#     for i in range(len(d),0,-1): #거꾸로 세보기
#         for combi in combinations(d,i):
#             if sum(combi) <= budget:
#                 answer += i
#                 stop_outer = True
#                 break
#         if stop_outer:
#             break

#     return answer
